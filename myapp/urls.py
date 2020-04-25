from django.urls import path
from .views import MyFirstView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
   path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
   path('', MyFirstView.as_view(), name='index'),
   path('create/', PostCreateView.as_view(), name='create'),
   path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
   path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]