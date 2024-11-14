from django import forms
from courses.models import Assignment, AssignmentRequirement, Submission



class AssignmentForm(forms.ModelForm):
    
    class Meta:
    
        model = Assignment

        fields =['title', 'description', "due_date"]


class AssignmentRequirementForm(forms.ModelForm):

    class Meta:
        model = AssignmentRequirement

        fields = ["requirement_text"]

class SubmissionForm(forms.ModelForm):
    # Ensure the link field is required
    submission_link = forms.URLField(
        required=True, 
        help_text="Provide the link to your submission.", 
        label="Submission Link"
    )

    class Meta:
        model = Submission
        fields = ['submission_link']  # Make sure this field matches the field in your model

    def clean_submission_link(self):
        link = self.cleaned_data.get('submission_link')
        if not link:
            raise forms.ValidationError("A valid submission link must be provided.")
        return link

class GradeSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['grade', 'feedback']