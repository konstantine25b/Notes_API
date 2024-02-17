from django.contrib import admin
from django.urls import path 
from .views import NoteList

urlpatterns = [
    path('notes/' , NoteList.as_view())
]
