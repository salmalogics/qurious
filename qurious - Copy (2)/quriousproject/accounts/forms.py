
from django import forms
from .models import*

class MemberForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for memberForm."""

        model = Member
        fields = '__all__'
        help_text={
            'username':None
        }
