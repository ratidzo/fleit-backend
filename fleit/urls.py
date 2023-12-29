from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    r'destinations', views.DestinationViewSet, basename='destinations')

urlpatterns = [
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            }
        )
    ]
