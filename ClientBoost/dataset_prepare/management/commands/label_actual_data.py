from django.core.management.base import BaseCommand
from dataset_prepare.models import Review, ProblemLabel


class Command(BaseCommand):
    help = 'Label reviews with BERT-Banking77 model from hugging face'

    def handle(self, *args, **options):
        from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
        tokenizer = AutoTokenizer.from_pretrained("philschmid/BERT-Banking77")
        model = AutoModelForSequenceClassification.from_pretrained("philschmid/BERT-Banking77")
        classifier = pipeline('text-classification', tokenizer=tokenizer, model=model)
        reviews_not_labeled = Review.objects.filter(label__isnull=True)
        for review in reviews_not_labeled:
            output = classifier(review.text)
            label_name = output[0]["label"]
            label = ProblemLabel.objects.get_or_create(name=label_name)[0]
            review.label = label
            review.save()
