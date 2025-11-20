from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializer import Snippet_Serializer

# Create your views here.

@csrf_exempt
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
        return JsonResponse(serializer.data , safe=False)
    
    elif req.method == "POST" :
        data = JSONParser().parse(req)
        serializer = Snippet_Serializer(data=data)
        if  serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors , status = 400)
    
@csrf_exempt
def snippet_detail(req , pk):
    try :
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist :
        return JsonResponse({"error" : "Snippet Not Found!!"} , status=404)
    
    if req.method == "GET":
        serializer = Snippet_Serializer(snippet)
        return JsonResponse(serializer.data)
    
    elif req.method == "PUT" :
        data = JSONParser().parse(req)
        serializer = Snippet_Serializer(snippet, data=data)
        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors , status=400)
    
    elif req.method == "DELETE":
        snippet.delete()
        return JsonResponse({"msg" : "snippet successfully deleted!!"} , status= 204)
    
    
        