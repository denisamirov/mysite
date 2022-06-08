from django.forms import ModelForm
from .models import Registration


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ('first_name',
                  'last_name',
                  'age',
                  'about',
                  'way',
                  'email',
                  'phone_number')