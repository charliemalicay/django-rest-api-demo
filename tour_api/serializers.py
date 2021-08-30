import re
from rest_framework import serializers

from tour_api.models import Package, Booking, WishlistItem


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


class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ['url', 'id', 'session_id', 'package', 'added_to_cart']
