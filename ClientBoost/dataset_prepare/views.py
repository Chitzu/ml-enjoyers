from rest_framework.viewsets import ModelViewSet
from .models import Review, Bank
from .serializers import ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @action(methods=["GET"], detail=False)
    def get_banks_id(self, request, *args, **kwargs):
        banks = Bank.objects.all().values("name", "id")
        return Response(banks)