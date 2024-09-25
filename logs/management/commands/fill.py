import urllib.request
from datetime import datetime

from django.core.management import BaseCommand

from logs.models import Log


class Command(BaseCommand):
    """
    Кастомная команда для заполнения БД
    """
    def handle(self, *args, **options):
        logo = urllib.request.urlopen(
            "https://drive.google.com/uc?id=18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp&export=download").read()
        str_ = logo.decode()
        file_logs = str_.split("\n")
        for  file_log in file_logs:
            if file_log != '':
                dict_ = eval(file_log)
                if dict_['bytes'] < 1000000000:
                    time = datetime.strptime(dict_['time'], '%d/%b/%Y:%H:%M:%S %z')
                    log = Log.objects.create(
                        ip_address=dict_['remote_ip'],
                        date = time,
                        http_method = dict_['request'],
                        uri_request = dict_['agent'],
                        code = dict_['response'],
                        size = dict_['bytes']
                    )

                    log.save()
        print('Логи загружены в БД')
