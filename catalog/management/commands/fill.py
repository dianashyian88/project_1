from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'name': 'Бокалы Bohemia',
             'description': 'Набор хрустальных бокалов для шампанского 6 шт.',
             'category_id': 1,
             'price': 1200},
            {'name': 'Туфли женские лодочки',
             'description': 'Туфли женские лодочки из натуральной кожи, цвет белый, каблук 11 см',
             'category_id': 2,
             'price': 8560},
            {'name': 'Полотенце для кухни',
             'description': 'Кухонное хлопковое полотенце размером 20Х50 см., цвет бордовый',
             'category_id': 3,
             'price': 95}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)
