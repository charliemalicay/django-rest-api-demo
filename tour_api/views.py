from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.reverse import reverse

from tour_api.models import Package, Booking
from tour_api.serializers import PackageSerializer, BookingSerializer


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


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [BasePermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
