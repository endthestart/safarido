from django.contrib import admin

from .models import Todo, TodoList


class TodoListAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Todo)
admin.site.register(TodoList, TodoListAdmin)
