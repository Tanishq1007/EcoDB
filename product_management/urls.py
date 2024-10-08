from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, ProductViewSet
from .views import SignupView, LoginView
router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
