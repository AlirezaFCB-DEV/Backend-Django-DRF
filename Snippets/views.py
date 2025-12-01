from rest_framework import viewsets
from .models import Snippet
from .serializer import Snippet_Serializer , User_Serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User

class User_ViewSet(viewsets.ModelViewSet) :
    queryset  = User.objects.all()
    serializer_class = User_Serializer
    
class Snippet_ViewSet(viewsets.ModelViewSet) :
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    