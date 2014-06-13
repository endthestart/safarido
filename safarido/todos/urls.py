from django.conf.urls import patterns, url

from .views import TodoListView, TodoListDetail

urlpatterns = patterns('',
    url(regex=r'^list/$', view=TodoListView.as_view(), name='todo_list_view'),
    url(regex=r'^list/(?P<pk>[0-9]+)/$', view=TodoListDetail.as_view(), name='todo_list_detail_view'),
)
