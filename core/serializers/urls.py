from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('credsapi',views.credsapi)


urlpatterns = router.urls