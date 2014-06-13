from django.conf.urls import patterns, url

from .views import TodoListView, TodoListDetail

urlpatterns = patterns('',
    url(regex=r'^list/$', view=TodoListView.as_view(), name='todo_list_view'),
    url(regex=r'^list/(?P<slug>[\w-]+)/$', view=TodoListDetail.as_view(), name='todo_list_detail_view'),
)
