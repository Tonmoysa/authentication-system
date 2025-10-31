from django.urls import path,include
from .views import UserListView

urlpatterns = [
   path('user/',UserListView.as_view(),name='user')
    
]
