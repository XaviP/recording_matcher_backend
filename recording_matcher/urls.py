from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers

from sound_recordings.serializers import SoundRecordingViewSet, \
    SoundRecordingInputViewSet

router = routers.DefaultRouter()
router.register(r'sound_recording', SoundRecordingViewSet)
router.register(r'input', SoundRecordingInputViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
