from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']

    def clean_title(self):
        data = self.cleaned_data['title']
        # The maximum length of the title is 50 characters
        if len(data) > 50:
            raise forms.ValidationError("The title cannot exceed 50 characters.")
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        # The maximum length of the description is 200 characters
        if len(data) > 500:
            raise forms.ValidationError("The description cannot exceed 200 characters.")
        return data
