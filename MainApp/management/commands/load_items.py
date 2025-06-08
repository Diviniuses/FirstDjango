from django.core.management.base import BaseCommand
from MainApp.models import Item

class Command(BaseCommand):
    help = 'Loads test items into the database'

    def handle(self, *args, **kwargs):
        items = [
            {"name": "Кроссовки abibas", "quantity": 5},
            {"name": "Куртка кожаная", "quantity": 3},
            {"name": "Соса-сola 1 литр", "quantity": 10},
            {"name": "Картофель фри", "quantity": 7},
            {"name": "Кепка", "quantity": 0}
        ]
        for item_data in items:
            Item.objects.get_or_create(
                name=item_data["name"],
                defaults={"quantity": item_data["quantity"]}
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded test items')) 