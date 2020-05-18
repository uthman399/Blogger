from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    to = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    comments = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': "form-control"
        }
    ))

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class SearchForm(forms.Form):
    query = forms.CharField()


from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email',)
