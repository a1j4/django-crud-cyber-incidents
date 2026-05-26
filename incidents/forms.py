from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident

        fields = [
            'title',
            'description',
            'severity',
            'resolved'
        ]

    def clean_title(self):
        title = self.cleaned_data['title']

        if not title.strip():
            raise forms.ValidationError(
                "El título no puede estar vacío"
            )

        return title

    def clean_description(self):
        description = self.cleaned_data['description']

        if not description.strip():
            raise forms.ValidationError(
                "La descripción no puede estar vacía"
            )

        return description