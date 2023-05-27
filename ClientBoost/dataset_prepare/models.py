from django.db import models


class ProblemLabel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Bank(models.Model):
    name = models.CharField(max_length=50)
    client_proportion = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} - {self.client_proportion}"


class Review(models.Model):
    text = models.TextField()
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True, related_name="reviews")
    label = models.ForeignKey(ProblemLabel, on_delete=models.SET_NULL, null=True, blank=True, related_name="reviews")

    def __str__(self):
        return f"{self.text} {self.bank} {self.label}"


