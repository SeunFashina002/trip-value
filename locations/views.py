from .models import State, Terminal, Trips
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.db.models import Q
from .serializers import StateSerializer, TerminalSerializer, TripSerializer, ParkTerminalSerializer



# Create your views here.

# endpoint for the search 
# http://127.0.0.1:8000/api/v1/terminals/?query=   this endpoint contains both terminals and state
# http://127.0.0.1:8000/api/v1/state/?query=   this endpoint contains only state


class StateList(ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class= StateSerializer

    def get_queryset(self):
        qs = State.objects.all()
        query = self.request.query_params.get('query')
        if query is not None:
            qs = State.objects.filter(
                Q(name__icontains=query)
            )
        return qs
    

class StateDetail(RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class= StateSerializer


class TerminalList(ListCreateAPIView):
    queryset = Terminal.objects.all()
    serializer_class= TerminalSerializer


    def get_queryset(self):
        queryset = Terminal.objects.all()
        query = self.request.query_params.get('query')
        if query is not None:
            queryset = Terminal.objects.filter(
                Q(name__icontains=query) | Q(state__name__icontains=query)
            )
        return queryset
    
class TerminalDetail(RetrieveUpdateDestroyAPIView):
    queryset = Terminal.objects.all()
    serializer_class= TerminalSerializer


# View for the Trips

class TripsList(ListCreateAPIView):
    queryset = Trips.objects.order_by('created_at')[:8]
    serializer_class = TripSerializer


class TripDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trips.objects.all()
    serializer_class= TripSerializer

class ParkList(ListAPIView):
    queryset = Terminal.objects.all()[:3]
    serializer_class= ParkTerminalSerializer



