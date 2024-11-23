from django import forms
from courses.models import Opportunities


class opportunityForm(forms.ModelForm):

    class Meta:

        model = Opportunities

        fields = ['title', 'description', 'link', 'dateline']