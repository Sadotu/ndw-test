# djangoProject/forms.py

from django import forms
from djangoProject.models.bridge_administration import BridgeAdministration


class BridgeAdministrationForm(forms.ModelForm):
    class Meta:
        model = BridgeAdministration
        fields = ['name', 'location', 'ris_index', 'vild_location']  # Add all the fields you need
