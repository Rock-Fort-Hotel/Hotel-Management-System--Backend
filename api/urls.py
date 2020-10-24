from django.urls import path

from api.views import reportViewSet,confirmationViewSet,outstandingViewSet,outstandingViewSetStatus,confirmViewSetStatus

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


#sajini
router.register(r'reportR',reportViewSet, basename='reportR' )
router.register(r'confirmation', confirmationViewSet, basename='confirmation')
router.register(r'outstanding', outstandingViewSet, basename='outstanding')
router.register(r'outstandingStatus', outstandingViewSetStatus, basename="outstat")
router.register(r'confirmStatus',confirmViewSetStatus,basename="constat")
#sajini


urlpatterns = router.urls