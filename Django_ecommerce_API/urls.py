from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views as core_views
from rest_framework.authtoken.views import obtain_auth_token
from ecommerce import views as ecommerce_views

router= routers.DefaultRouter()
router.register(r'item', ecommerce_views.ItemViewSet, basename='item')
router.register(r'order', ecommerce_views.OrderViewSet, basename='order')

urlpatterns= router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
]
