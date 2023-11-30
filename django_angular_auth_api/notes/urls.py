from django.conf.urls import url
from django.urls import path, include
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('todo', TodoListApiView.as_view()),
    path('todo/<int:todo_id>/', TodoDetailApiView.as_view()),
]