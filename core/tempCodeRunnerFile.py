
class PersonalDomainForm(forms.Form):

    full_name = forms.CharField(

    max_length=100,

    label="Full Name",

    initial="Sambhav Acharya",

    widget=forms.TextInput(attrs={

        "class": input_class,

        "placeholder": "Enter your full name"

    })

)