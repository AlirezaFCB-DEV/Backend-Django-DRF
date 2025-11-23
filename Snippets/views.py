from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializer import Snippet_Serializer

# Create your views here.

@api_view(["GET" , "POST"])
def snippet_list(req) :
    """
    List all code snippets or create a new one.

    GET:
        Returns a list of all code snippets

    POST:
        Creates a new code snippet
        Expects the request body to contain a JSON object with the following
        structure:
        {
            "title": "string",
            "code": "string",
            "linenos": boolean,
            "language": "string",
            "style": "string"
        }
        Returns the newly created code snippet
    """
    if  req.method == "GET" :
        snippets = Snippet.objects.all()
        serializer = Snippet_Serializer(snippets , many=True)
        return Response(serializer.data)
    
    elif req.method == "POST" :
        serializer = Snippet_Serializer(data=req.data)
        if  serializer.is_valid() :
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET" , "PUT" , "DELETE"])
def snippet_detail(req , pk):
    try :
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist :
        return Response({"error" : "Snippet Not Found!!"} , status=status.HTTP_404_NOT_FOUND)
    
    if req.method == "GET":
        serializer = Snippet_Serializer(snippet)
        return Response(serializer.data)
    
    elif req.method == "PUT" :
        serializer = Snippet_Serializer(snippet, data=req.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    elif req.method == "DELETE":
        snippet.delete()
        return Response({"msg" : "snippet successfully deleted!!"} , status=status.HTTP_204_NO_CONTENT)
    
    
        