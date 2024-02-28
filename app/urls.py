from django.urls import path 
from .views import add , get , get_all , delete , updete

urlpatterns = [
    path('add/' , add),
    path('get/<int:pk>/' , get ),
    path('get/all/' , get_all ),
    path('delete/<int:pk>/' , delete ),
    path('updete/' , updete ),
]