from rest_framework import serializers
from .models import Profile, Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'profile_pic', 'bio', 'country', 'email')