from django.urls import path
from .views import StateList, StateDetail, TerminalList, TerminalDetail, TripsList, TripDetail, ParkList

urlpatterns = [
    path('state/', StateList.as_view(), name='state-list'),
    path('state/<int:pk>/', StateDetail.as_view(), name='state-detail'),
    path('terminals/', TerminalList.as_view(), name='terminal-list'),
    path('terminals/<int:pk>/', TerminalDetail.as_view(), name='terminal-detail'),
    path('latest-trips/', TripsList.as_view(), name='latest-trips'),
    path('latest-trips/<int:pk>/', TripDetail.as_view(), name='latest-trip-detail'),
    path('parks/', ParkList.as_view(), name='parks'),
]

# / --> represents all item/objects
# /<int:pk>/ --> represents single item/objects