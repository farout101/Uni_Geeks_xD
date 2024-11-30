from django.forms import ModelForm
from . models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # This will create the form with all of the metadata from the model.
        