from rest_framework import serializers 
from slqe.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'phone',
                  'url',
                  'name',
                  'role')