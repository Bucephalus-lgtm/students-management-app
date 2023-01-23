from django import forms
from .models import student


class studentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(studentForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
