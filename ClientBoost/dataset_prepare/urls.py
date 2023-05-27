from rest_framework import routers
from .views import ReviewViewSet


router = routers.SimpleRouter()
router.register("review", ReviewViewSet)

urlpatterns = router.urls