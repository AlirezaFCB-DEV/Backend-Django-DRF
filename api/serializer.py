from rest_framework import serializers
from .models import Profile

class Profile_Serializer(serializers.ModelSerializer) :
    class Meta :
        model = Profile
        fields = ["id" , "user" , "bio" , "age"]
        
        