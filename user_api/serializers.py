from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    packages = serializers.HyperlinkedRelatedField(many=True, view_name='package-detail', read_only=True)
    bookings = serializers.HyperlinkedRelatedField(many=True, view_name='booking-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets', 'packages', 'bookings']
