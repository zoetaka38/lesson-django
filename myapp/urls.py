from django.urls import path
from .views import MyFirstView

urlpatterns = [
    path('', MyFirstView.as_view())  # URLとViewを組み合わせる！
]