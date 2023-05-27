from django.core.management.base import BaseCommand
from dataset_prepare.models import Review, Bank


class Command(BaseCommand):
    help = 'Add bank'

    def handle(self, *args, **options):
        import numpy as np
        banks_id = list(Bank.objects.all().values_list("id", flat=True))
        bank_proportions = list(Bank.objects.all().values_list("client_proportion", flat=True))
        bank_proportions = [num / 100 for num in bank_proportions]
        reviews_count = Review.objects.count()
        generated_values = np.random.choice(banks_id, size=reviews_count, p=bank_proportions)
        reviews = list(Review.objects.all())
        for i in range(reviews_count):
            review = reviews[i]
            review.bank_id = generated_values[i]
            review.save()