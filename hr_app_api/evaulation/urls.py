from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_evaulation, name='create-evaulation'),
    path('update/<int:pk>',views.update_evaulation, name='update-evaulation'),
    path('delete/<int:pk>', views.delete_evaulation, name='delete-evaulation'),
    path('evaulation/<int:pk>', views.view_evaulation, name='view-evaulation'),
    path('evaulations/',views.view_all_evaulations, name='view-all-applications')
]
