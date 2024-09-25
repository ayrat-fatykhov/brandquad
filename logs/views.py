from rest_framework import generics

from logs.models import Log
from logs.paginators import LogPaginator
from logs.serializers import LogSerializer


class LogListAPIView(generics.ListAPIView):
    """
    Отвечает за отображение списка Логов.
    """
    serializer_class = LogSerializer
    queryset = Log.objects.all()
    pagination_class = LogPaginator


class LogRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за отображение одного Лога.
    """
    serializer_class = LogSerializer
    queryset = Log.objects.all()
