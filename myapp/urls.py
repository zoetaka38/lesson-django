from django.urls import path
from .views import MyFirstView, PostCreateView, PostDetailView

urlpatterns = [
   path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
   path('', MyFirstView.as_view(), name='index'),
   path('create/', PostCreateView.as_view(), name='create')
]