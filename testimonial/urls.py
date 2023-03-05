from django.urls import path
from .views import TestimonyList, TestimonyDetail


urlpatterns = [
    path('testimonial/', TestimonyList.as_view(), name='testimony-list'),
    path('testimonial/<int:pk>/', TestimonyDetail.as_view(), name='testimony-detail'),
]