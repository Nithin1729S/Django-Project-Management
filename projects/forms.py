from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','featured_img','desc','demo_link','src_link','tags']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
            
        }

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        # self.fields['desc'].widget.attrs.update({'class':'input','placeholder':'Add Description'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})