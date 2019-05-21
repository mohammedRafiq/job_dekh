from django import forms

YEARS_OF_EXPERIENCE = (
    ("Fresher", "Fresher"),
    ("Years 1-2", "Years 1-2"),
    ("Years 2-5", "Years 2-5"),
    ("Years 5-8", "Years 5-8"),
    ("Years 8-10", "Years 8-10"),
    ("Years 10+", "Years 10+")
)

class PostJob(forms.Form):
      designation = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label="Designation")
      employer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Employer Name'}))
      years_of_experience = forms.ChoiceField(choices=YEARS_OF_EXPERIENCE)
      location = forms.CharField(label='Location',widget=forms.TextInput(attrs={'placeholder': 'Job Location'}))
      title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Job Title'}),label='Job Title')
      description = forms.CharField(widget=forms.Textarea(attrs={'width':"80%",'cols' : "80", 'rows': "20", }))
