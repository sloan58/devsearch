from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'featured_image',
            'demo_link',
            'source_link',
            'tags'
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }
