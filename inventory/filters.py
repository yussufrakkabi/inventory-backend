from django_filters import rest_framework as filters
from .models import Inventory

class InventoryFilter(filters.FilterSet):
    # Filtering by category (case-insensitive)
    category = filters.CharFilter(field_name='product__category__name', lookup_expr='icontains')
    
    # Filtering by minimum price
    price_min = filters.NumberFilter(field_name='product__price', lookup_expr='gte')
    
    # Filtering by maximum price
    price_max = filters.NumberFilter(field_name='product__price', lookup_expr='lte')
    
    # Filtering by low stock (items with quantity less than 10, for example)
    low_stock = filters.BooleanFilter(method='filter_low_stock')

    class Meta:
        model = Inventory
        fields = ['category', 'price_min', 'price_max', 'low_stock']

    def filter_low_stock(self, queryset, name, value):
        if value:
            # Define your threshold for low stock, e.g., quantity less than 10
            return queryset.filter(quantity__lt=10)
        return queryset
