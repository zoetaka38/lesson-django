from django.urls import path
from .views import MyFirstView, PostCreateView

urlpatterns = [
   path('', MyFirstView.as_view(), name='index'),  # URLとViewを組み合わせる！
   path('create/', PostCreateView.as_view(), name='create')
]