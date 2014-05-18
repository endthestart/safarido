from django.conf.urls import patterns, url

from .views import TodoListView, TodoListDetailView

urlpatterns = patterns(
    '',
    url(
        regex=r'^list/(?P<slug>[\w-]+)/$',
        view=TodoListDetailView.as_view(),
        name='todos_todo-list_detail',
    ),
    url(
        regex=r'^$',
        view=TodoListView.as_view(),
        name='todos_todo-list_list',
    ),
)
