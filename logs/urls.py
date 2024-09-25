from django.urls import path

from logs.apps import LogsConfig
from logs.views import LogListAPIView, LogRetrieveAPIView

app_name = LogsConfig.name

urlpatterns = [
    path('', LogListAPIView.as_view(), name='log_list'),
    path('log/view/<int:pk>/', LogRetrieveAPIView.as_view(), name='log_view'),
]