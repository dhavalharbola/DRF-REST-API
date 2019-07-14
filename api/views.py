from django.shortcuts import render
from todo.models import Todo
from api.serializers import TodoSerializer
from rest_framework import generics

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class =TodoSerializer