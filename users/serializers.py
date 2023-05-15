from rest_framework import serializers

from users.models import MaralUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaralUser
        fields = ('email', 'first_name', 'last_name', 'active')
