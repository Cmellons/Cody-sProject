from django.core.management.base import BaseCommand
from stocks.models import Stock

class Command(BaseCommand):
    help = 'Deletes all stock records from the database'

    def handle(self, *args, **options):
        Stock.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All stock records have been deleted successfully'))
        