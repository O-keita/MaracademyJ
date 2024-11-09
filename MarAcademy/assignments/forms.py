from django import forms
from courses.models import Assignment, AssignmentRequirement



class AssignmentForm(forms.ModelForm):
    
    class Meta:
    
        model = Assignment

        fields =['title', 'description', "due_date"]


class AssignmentRequirementForm(forms.ModelForm):

    class Meta:
        model = AssignmentRequirement

        fields = ["requirement_text"]