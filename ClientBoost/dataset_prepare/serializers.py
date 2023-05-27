from rest_framework import serializers
from .models import Review, Bank


class ReviewSerializer(serializers.ModelSerializer):
    bank_id = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ("text", "bank_id")