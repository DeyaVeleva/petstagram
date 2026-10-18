from django import forms
from pets.models import Pet
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['slug']
        widgets = {
            'name':forms.TelInput(attrs={'placeholder':'Pet name'}),
            'date_of_birth':forms.DateInput(attrs={'type':'date'}),
            'personal_photo':forms.TextInput(attrs={'placeholder':'Link to image'}),
        }
        labels = {
            'name':'Pet Name',
            'date_of_birth':'Date of Birth',
            'personal_photo':'Link to Image',
        }

class PetDeleteForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disables'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
