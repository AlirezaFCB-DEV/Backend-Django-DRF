from rest_framework import viewsets , renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Snippet
from .serializer import Snippet_Serializer , User_Serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User

@api_view(["GET"])
def api_root(req , format=None) :
    return Response({
        "users" : reverse("user-list" , request=req, format=format),
        "snippets" : reverse("snippets-list" , request=req , format=format)
    })

class User_ViewSet(viewsets.ModelViewSet) :
    queryset  = User.objects.all()
    serializer_class = User_Serializer
    
class Snippet_ViewSet(viewsets.ModelViewSet) :
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, renderer_classes = [renderers.StaticHTMLRenderer])
    def highlight(self, req , *args , **kwargs) :
        snippet = self.get_object()
        return Response(snippet.code)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    