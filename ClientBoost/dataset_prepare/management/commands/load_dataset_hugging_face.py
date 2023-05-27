from django.core.management.base import BaseCommand
from dataset_prepare.models import Review


class Command(BaseCommand):
    help = 'Load review data from hugging face'

    def handle(self, *args, **options):
        from datasets import load_dataset
        reviews = load_dataset("dvilasuero/banking_app")["train"].to_pandas()
        print(reviews.text)
        for review in reviews.text:
            print(review)
            Review.objects.get_or_create(text=review)