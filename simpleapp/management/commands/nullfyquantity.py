from django.core.management.base import BaseCommand, CommandError
from simpleapp.models import Product


class Command(BaseCommand):
    help = 'Обнуляет товары' # показывает подсказку при вводе "python manage.py <ваша команда> --help"

    requires_migrations_cheks = True # напоминать ли о миграциях.
    # Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def handle(self,*args, **options):
        # здесь можете писать любой код, который выполняется при вызове вашей команды
        self.stdout.readable()
        self.stdout.write('Вы хотите удалить продукты? yes/no')  # спрашиваем пользователя
        # действительно ли он хочет удалить все товары
        answer = input() # считываем подтверждение

        if answer == 'yes': # в случае подтверждения действительно удаляем все товары
            Product.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Продукты успешно удалены'))
            return

        self.stdout.write(self.style.ERROR('В доступе отказано')) # в случае
        # неправильного подтверждения, говорим что в доступе отказано

