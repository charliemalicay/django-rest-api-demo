from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.reverse import reverse

from tour_api.filters import PackagePriceFilter
from tour_api.models import Package, Booking, WishlistItem
from tour_api.serializers import PackageSerializer, BookingSerializer, WishlistItemSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tour-package': reverse('tour-package-list', request=request, format=format)
    })


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [BasePermission]
    search_fields = ('name', 'category', 'promo')
    ordering_fields = ('id', 'name', 'price', 'rating', 'tour_length', 'start')
    filter_backends = [PackagePriceFilter, SearchFilter, OrderingFilter]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [BasePermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WishlistItemViewSet(viewsets.ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    permission_classes = [BasePermission]
    session_id = 'wishlist-items'

    def perform_create(self, serializer):
        serializer.save(session_id=self.session_id)

    def perform_destroy(self, instance):
        instance.delete()
