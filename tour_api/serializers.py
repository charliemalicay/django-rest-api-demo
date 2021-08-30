import re
from rest_framework import serializers

from tour_api.models import Package, Booking


class PackageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Package
        fields = ['url', 'id', 'owner', 'category', 'name', 'promo', 'price', 'rating',
                  'tour_length', 'start', 'thumbnail_url']


class BookingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Booking
        fields = ['url', 'id', 'owner', 'name', 'email_address', 'street_address', 'city', 'package']
