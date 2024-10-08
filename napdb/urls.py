from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product_management.views import BrandViewSet, ProductViewSet
from django.contrib import admin
from django.urls import path, include
from product_management.views import home
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('product_management.urls')),  # Assuming this is where your app's API endpoints are
    path('', home),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
