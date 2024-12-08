from rest_framework.serializers import ModelSerializer
from project.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__' # This will return all fields in the model