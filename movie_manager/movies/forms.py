from django.forms import ModelForm
from .models import MovieInfo,Director

class MovieForm(ModelForm):
    class Meta:
        model =MovieInfo
        fields ='__all__'


class DirectorForm(ModelForm):
    class Meta:
        model =Director
        fields ='__all__'
