from django.core.management.base import BaseCommand, CommandError
from shoes.models import Manufacturer, ShoeType, ShoeColor

colors = [
    'RED', 'ORANGE', 'YELLOW',
    'GREEN', 'BLUE', 'INDIGO',
    'VIOLET', 'WHITE', 'BLACK'
]

shoe_types = [
    'Sneaker', 'Boot', 'Sandal',
    'Dress', 'Other'
]

class Command(BaseCommand):
    help = 'Pre-populate database with information about shoes'

    def _build_database(self):
        for idx, color in enumerate(colors):
            new_color = ShoeColor(idx, color)
            new_color.save()
        
        for idx, st in enumerate(shoe_types):
            new_type = ShoeType(idx, st)
            new_type.save()
    
    def handle(self, *args, **kwargs):
        self._build_database()