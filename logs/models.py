from django.db import models


class Log(models.Model):
    """
    Определят поля для модели Лог
    """
    ip_address = models.CharField(max_length=255, verbose_name='IP-адрес')
    date = models.DateTimeField(verbose_name='дата из лога')
    http_method = models.CharField(max_length=255, verbose_name='http метод')
    uri_request = models.CharField(max_length=255, verbose_name='uri запроса')
    code = models.IntegerField(verbose_name='код ответа')
    size = models.IntegerField(verbose_name='размер ответа')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Лог
        """
        return f'Лог - {self.ip_address}, {self.date}, {self.http_method}, {self.uri_request}, {self.code}, {self.size}'

    class Meta:
        """
        Определяет отображение модели Лог в админке. Сортирует по порядковому номеру.
        """
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('pk',)
