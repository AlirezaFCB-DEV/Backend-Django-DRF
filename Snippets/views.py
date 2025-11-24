from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Snippet
from .serializer import Snippet_Serializer

# Create your views here.

class Snippet_List(APIView):
    def get(self, req):
        snippets = Snippet.objects.all()
        serializer = Snippet_Serializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = Snippet_Serializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Snippet_Detail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, req, pk):
        snippet = self.get_object(pk)
        serializer = Snippet_Serializer(snippet)
        return Response(serializer.data)

    def put(self, req, pk):
        snippet = self.get_object(pk)
        serializer = Snippet_Serializer(snippet, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response({"msg": "snippet successfully deleted!!"}, status=status.HTTP_204_NO_CONTENT)
