from guardian.shortcuts import get_objects_for_user

from rest_framework import generics
from rest_framework.filters import DjangoObjectPermissionsFilter

from .permissions import SafaridoObjectPermissions
from .models import TodoList, Todo
from .serializers import TodoListSerializer, TodoSerializer


class TodoListView(generics.ListCreateAPIView):
    """
    List all Todo Lists, or create a new Todo List.
    """
    model = TodoList
    serializer_class = TodoListSerializer

    def get_queryset(self):
        return get_objects_for_user(self.request.user, 'view_todolist', klass=TodoList)

    def pre_save(self, obj):
        obj.owner = self.request.user


class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a TodoList instance.
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (SafaridoObjectPermissions,)

    def pre_save(self, obj):
        obj.owner = self.request.user
