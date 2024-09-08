from django import forms

# Creating email form

class EmailPostForm(forms.Form):
    #Cearting fields for form
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    
    