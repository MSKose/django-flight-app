from django.shortcuts import render
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from rest_framework import viewsets
from .models import Flight, Passenger, Reservation
from .permissions import IsStafforReadOnly

# Create your views here.


# GET, POST, PUT, DELETE, PATCH
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)

    '''
    I'm just gonna paste the source code comments for get_serializer_class:

    Returns the class to use for the serializer.
    Defaults to using `self.serializer_class`.

    You may want to override this if you need to provide different
    serializations depending on the incoming request.
    '''

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer # why tho? since we want our staff user to see all the fields including that of Reservation models' for the flight/flights/ endpoint
        return serializer # else, just return the FlightSerializer, which only returns the Flight fields and nothing related to Reservation

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    '''
    as the source code in GenericAPIView states, get_queryset returns a list of items that is specific to the user.
    and since we want to change the behavior in who can see what
    '''

    def get_queryset(self):
        queryset = super().get_queryset() # super here takes the queryset we have already defined above
        if self.request.user.is_staff: # return every object if admin
            return queryset
        return queryset.filter(user=self.request.user) # else, return tje list of objects only if the user is the creator