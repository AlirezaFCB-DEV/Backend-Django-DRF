from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "Snippets"
snippet_list = views.Snippet_ViewSet.as_view({"get": "list", "post": "create"})
snippet_detail = views.Snippet_ViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})

urlpatterns = [
    # path("snippets/",
    #      views.Snippet_List.as_view({"get": "list", "post": "create"})),
    # path("snippets/<int:pk>/", views.Snippet_Detail.as_view(
    #     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})), #! Bad CODE
    path("snippets/" , snippet_list , name="snippet-list"),
    path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    path("users/", views.User_List.as_view()),
    path("users/<int:pk>/", views.User_Detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)