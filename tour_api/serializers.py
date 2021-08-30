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
    STREET_ADDRESS_ERROR = 'Street address must be in the format "11 Abc St."'

    class Meta:
        model = Booking
        fields = ['name', 'email_address', 'street_address', 'city', 'package']

    def validate_street_address(self, value):
        regexp = re.compile(r'\d+ \w+ \w+')
        if regexp.search(value):
            return value
        raise serializers.ValidationError(
            self.STREET_ADDRESS_ERROR
        )
