from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_application,name='create-application'),
    path('update/<int:pk>', views.update_application, name='update-application'),
    path('delete/<int:pk>', views.delete_application, name='delete-application'),
    path('application/<int:pk>', views.view_application, name='view-application'),
    path('applications/',views.view_all_applications,name='view-all-applications')
]
