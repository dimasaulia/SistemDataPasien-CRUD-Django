from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:update_id>', views.update, name='update'),
    path('delete/<int:delete_id>', views.delete, name='delete'),
]
