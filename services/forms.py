from django import forms
from .models import Services

#employee form
#modelForm -->it will create form using model fileds
class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'