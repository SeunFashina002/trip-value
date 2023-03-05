from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TestimonialSerializer
from .models import Testimonial


# Create your views here.

class TestimonyList(ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer



class TestimonyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
