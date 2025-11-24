from rest_framework import generics
from .models import Snippet
from .serializer import Snippet_Serializer

# Create your views here.


class Snippet_List(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer


class Snippet_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer
