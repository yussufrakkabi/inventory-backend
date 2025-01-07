from rest_framework import generics, viewsets, permissions
from django.utils import timezone
from .models import (
    Category, Product, Supplier,
    Inventory, InventoryLog, Customer, Order
)
from .serializers import (
    CategorySerializer, ProductSerializer, SupplierSerializer, 
    InventorySerializer, InventoryLogSerializer, CustomerSerializer, OrderSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import action
from .filters import InventoryFilter
from django_filters.rest_framework import DjangoFilterBackend


# Category CRUD
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# Product CRUD
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


# Supplier CRUD
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]


# Customer CRUD
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Order CRUD
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


# Inventory CRUD and Tracking
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        # Track quantity changes
        if 'quantity' in serializer.validated_data:
            # Log the change
            InventoryLog.objects.create(
                product=instance.product_name,
                change_quantity=instance.quantity,
                updated_by=self.request.user,
                timestamp=timezone.now()
            )

    # Custom action to view inventory levels with optional filtering
    @action(detail=False, methods=['get'])
    def view_inventory_levels(self, request):
        queryset = self.get_queryset()

        # Apply filtering if provided (category, price range, low stock)
        category = request.query_params.get('category', None)
        low_stock = request.query_params.get('low_stock', None)

        if category:
            queryset = queryset.filter(product_name__category__name=category)
        if low_stock == 'true':
            queryset = queryset.filter(quantity__lt=5)  # Threshold for low stock

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Inventory filter
class InventoryLevelView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InventoryFilter


# InventoryLog for tracking changes
class InventoryLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer
    permission_classes = [permissions.IsAuthenticated]



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the inventory
        return obj.updated_by == request.user


# Overriding the create method to handle custom save logic
def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the validated data
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)