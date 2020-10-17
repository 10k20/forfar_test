from rest_framework.routers import DefaultRouter

from .views import PrinterViewSet, CheckViewSet


router = DefaultRouter()
router.register(r'printers', PrinterViewSet)
router.register(r'checks', CheckViewSet)

urlpatterns = router.urls