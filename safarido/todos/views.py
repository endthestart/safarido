from django.views.generic import ListView, DetailView

from .models import TodoList, Todo


class TodoListView(ListView):
    context_object_name = 'todo_lists'
    model = TodoList
    template_name = 'todos/todo-list_list.html'


class TodoListDetailView(DetailView):
    context_object_name = 'todo_list'
    model = TodoList
    template_name = 'todos/todo-list_detail.html'
