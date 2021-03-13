from django.urls import path
from .views import SnippetList

urlpatterns = [
    path('contact/', SnippetList.as_view()),
]
