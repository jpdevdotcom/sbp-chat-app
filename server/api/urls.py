from django.urls import path
from .views import RealtimeTokenView

urlpatterns = [
    path('realtime-token/', RealtimeTokenView.as_view()),
]
