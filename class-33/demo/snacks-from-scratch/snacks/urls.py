from django.urls import path
from .views import SnackListCreate, SnackRetrieveUpdateDestroy

urlpatterns = [
    path('', SnackListCreate.as_view(), name='snack_list_create'),
    path('<int:pk>/', SnackRetrieveUpdateDestroy.as_view(), name='snack_retrieve_update_destroy'),
]
