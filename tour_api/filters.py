from rest_framework.filters import BaseFilterBackend


class PackagePriceFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filters = {}
        price_min = request.query_params.get('price_min', None)

        if price_min:
            filters['price__gte'] = price_min

        price_max = request.query_params.get('price_max)', None)

        if price_max:
            filters['price__lte'] = price_max

        return queryset.filter(**filters)
