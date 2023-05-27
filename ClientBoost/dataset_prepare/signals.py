from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Review


@receiver(pre_save, sender=Review)
def add_label_to_review(sender, instance: Review, created, **kwargs):
    if created:
        from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
        tokenizer = AutoTokenizer.from_pretrained("philschmid/BERT-Banking77")
        model = AutoModelForSequenceClassification.from_pretrained("philschmid/BERT-Banking77")
        classifier = pipeline('text-classification', tokenizer=tokenizer, model=model)
        output = classifier(review.text)
        label_name = output[0]["label"]
        label = ProblemLabel.objects.get_or_create(name=label_name)[0]
        instance.label = label

