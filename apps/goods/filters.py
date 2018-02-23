import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilters(django_filters.rest_framework.FilterSet):
    '''
    商品的过虑类
    '''
    pricemin = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')
    # queryset, name, value都是默认传进来的

    def top_category_filter(self, queryset, name, value):
        # 满足任意一个分类都可以返回结果
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|
                               Q(category__parent_category__parent_category_id=value))
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
