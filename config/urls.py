from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from air_services.views import (
    KategoriyaViewSet, XizmatKorsatishNuqtasiViewSet, MahsulotViewSet,
    AviakompaniyaViewSet, ParvozViewSet, YolovchiViewSet,
    ChiptaViewSet, BagajViewSet, XodimViewSet,
    register_view
)

router = DefaultRouter()
router.register(r'kategoriyalar', KategoriyaViewSet)
router.register(r'xizmatlar', XizmatKorsatishNuqtasiViewSet)
router.register(r'mahsulotlar', MahsulotViewSet)
router.register(r'aviakompaniyalar', AviakompaniyaViewSet)
router.register(r'parvozlar', ParvozViewSet)
router.register(r'yolovchilar', YolovchiViewSet)
router.register(r'chiptalar', ChiptaViewSet)
router.register(r'bagajlar', BagajViewSet)
router.register(r'xodimlar', XodimViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register_view, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)