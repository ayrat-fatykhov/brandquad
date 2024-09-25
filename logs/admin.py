from django.contrib import admin

from logs.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """
    Отображает все поля, фильтрует по http методам, ищет логи по коду ответа в админке
    """
    list_display = ('pk', 'ip_address', 'date', 'http_method', 'uri_request', 'code', 'size')
    list_filter = ('http_method',)
    search_fields = ('code',)
