from rest_framework import serializers

from logs.models import Log


class LogSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность. Для модели Лог.
    """

    class Meta:
        model = Log
        fields = '__all__'
