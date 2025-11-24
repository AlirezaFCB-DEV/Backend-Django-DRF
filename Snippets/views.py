from rest_framework import mixins, generics
from .models import Snippet
from .serializer import Snippet_Serializer

# Create your views here.


class Snippet_List(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer
    def get(self, req):
        return self.list(req)

    def post(self, req):
        return self.create(req)


class Snippet_Detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin , mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer

    def get(self, req , *args, **kwargs):
        return self.retrieve(req , *args , **kwargs)

    def put(self, req, *args , **kwargs):
        return self.update(req , *args , **kwargs)
        

    def delete(self, req , *args , **kwargs):
        return self.destroy(req , *args , **kwargs)
        