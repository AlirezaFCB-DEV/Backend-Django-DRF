from rest_framework import generics
from rest_framework import viewsets
from .models import Snippet
from .serializer import Snippet_Serializer , User_Serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User

# Create your views here.
# class Snippet_List(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = Snippet_Serializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class Snippet_Detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = Snippet_Serializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

class  User_List(generics.ListAPIView) :
    queryset = User.objects.all()
    serializer_class = User_Serializer
    
class User_Detail(generics.RetrieveAPIView) :
    queryset = User.objects.all()
    serializer_class = User_Serializer
    
class Snippet_ViewSet(viewsets.ModelViewSet) :
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer