from django import forms
from material import *
from .models import Mitbringsel
from django.template import Template

MITBRINGSEL_TYPE_CHOICES = (
    ('Salat', 'Salat'),
    ('Dessert', 'Dessert')
)

class MitbringselForm(forms.ModelForm):
    class Meta:
        model = Mitbringsel
        fields = ['text', 'type']

    text = forms.CharField()
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=MITBRINGSEL_TYPE_CHOICES)
    definitiv = forms.BooleanField(required=False, label="Definitiv")

    title = 'Neues Mitbringsel'
    layout = Layout(
            Row('text'),
            Row('type'),
            Row('definitiv'),
        )
    template = Template("""
    {% form %}
        {% part form.definitiv add_group_class %}right-align{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="waves-effect waves-light btn" type="submit">Submit</button>
    """)
