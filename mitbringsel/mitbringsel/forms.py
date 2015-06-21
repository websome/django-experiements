from django import forms
from material import *
from .models import Mitbringsel, MitbringselType
from django.template import Template


class MitbringselForm(forms.ModelForm):
    class Meta:
        model = Mitbringsel
        fields = ['text', 'type']

    type = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=MitbringselType.objects.all(), empty_label=None)
    definitiv = forms.BooleanField(required=False, label="Definitiv")
    comment = forms.CharField(widget=forms.Textarea, required=False)

    title = 'Neues Mitbringsel'
    layout = Layout(
            Row('text'),
            Row('type'),
            Row('comment'),
            Row('definitiv'),
        )
    template = Template("""
    {% form %}
        {% part form.definitiv add_group_class %}right-align{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="waves-effect waves-light btn" type="submit">Hinzuf&uumlgen</button>
    """)
