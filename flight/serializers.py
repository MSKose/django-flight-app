from rest_framework import serializers
from .models import Flight, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = (
            "flight_number",
            "operating_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )

class PassengerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Passenger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    
    passenger = PassengerSerializer(many=True, required=True)
    flight = serializers.StringRelatedField()     # default read_only=True
    flight_id = serializers.IntegerField(write_only=True) # since we cannot create with flight (it's read-only) we had to create flight_id with write_only
    user = serializers.StringRelatedField()     # default read_only=True
    user_id = serializers.IntegerField(write_only=True, required=False)
    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",  # GET
            "flight_id",  # POST
            "user",  # GET
            "user_id",  # POST
            "passenger"
        )

    """
    My flight/resv/ endpoint's POST method requires a JSON like the following;
            {
                "flight_id": 0,
                "user_id": 0,
                "passenger": [
                {
                    "first_name": "string",
                    "last_name": "string",
                    "email": "user@example.com",
                    "phone_number": 0
                }
            ]
        }

    And since I want to save the passenger part to my Passenger model and not Reservation model
    I override the create method of this serializer like so;
    """    

    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        validated_data['user_id'] = self.context['request'].user.id # self.context['request'].user.id means the current authoenticated user
        reservation = Reservation.objects.create(**validated_data)
        
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()
        return reservation

class StaffFlightSerializer(serializers.ModelSerializer):

    '''
    how did we get access to reservation while the serializer uses Flight model?
    well we had a related_name named reservation in our Reservation model
    with a ForeignKey attached to Flight
    '''
    
    reservation = ReservationSerializer(many=True, read_only=True)
    class Meta:
        model = Flight
        fields = "__all__"