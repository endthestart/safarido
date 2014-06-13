from rest_framework import serializers
from .models import TodoList, Todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'created_on', 'title', 'slug', 'parent')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'created_on', 'list', 'title', 'description', 'assigned_to', 'due_date', 'is_done')
