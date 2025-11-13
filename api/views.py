from rest_framework import viewsets
from .models import Profile
from .serializer import Profile_Serializer


# Create your views here.

class Profile_View_Set(viewsets.ModelViewSet) :
    queryset = Profile.objects.all()
    serializer_class = Profile_Serializer
