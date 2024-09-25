from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Кастомная команда для создания суперпользователя
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='Admin',
            last_name='Admin',
            is_superuser=True,
            is_staff=True,
        )

        user.set_password('123qwe567rty')
        user.save()
