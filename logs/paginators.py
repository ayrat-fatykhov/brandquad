from rest_framework.pagination import PageNumberPagination


class LogPaginator(PageNumberPagination):
    """
    Выводит 10 логов на одной странице
    """
    page_size = 10
