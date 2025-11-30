from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "Snippets"
router = DefaultRouter()
router.register(r"snippets" , views.Snippet_ViewSet)

urlpatterns = [
    # path("snippets/",
    #      views.Snippet_List.as_view({"get": "list", "post": "create"})),
    # path("snippets/<int:pk>/", views.Snippet_Detail.as_view(
    #     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})), #! Bad CODE
    path("" , include(router.urls)),
    path("users/", views.User_List.as_view()),
    path("users/<int:pk>/", views.User_Detail.as_view()),
]
