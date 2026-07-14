from django import forms


# Common styling for normal inputs
input_class = (
    "w-full rounded-lg border border-gray-300 "
    "bg-white px-4 py-3 text-sm text-slate-900 "
    "placeholder-gray-400 "
    "focus:border-blue-600 focus:ring-2 focus:ring-blue-200 "
    "outline-none transition"
)


# Common styling for textareas
textarea_class = (
    "w-full rounded-lg border border-gray-300 "
    "bg-white px-4 py-3 text-sm text-slate-900 "
    "placeholder-gray-400 "
    "focus:border-blue-600 focus:ring-2 focus:ring-blue-200 "
    "outline-none transition resize-none"
)


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

    email = forms.EmailField(
        label="Email Address",
        initial="contact@bisup.com",
        widget=forms.EmailInput(attrs={
            "class": input_class,
            "placeholder": "Enter your email"
        })
    )

    phone = forms.CharField(
        max_length=20,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "Enter your phone number"
        })
    )

    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(attrs={
            "class": textarea_class,
            "placeholder": "Enter your address",
            "rows": 3
        })
    )

    citizenship_number = forms.CharField(
        max_length=50,
        label="Citizenship Number",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "Enter citizenship number"
        })
    )

    domain_name = forms.CharField(
        max_length=100,
        label="Domain Name",
        initial="bisup.com.np",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "example.com.np"
        })
    )

    purpose = forms.CharField(
        label="Purpose of Domain",
        widget=forms.Textarea(attrs={
            "class": textarea_class,
            "placeholder": "Explain the purpose of your domain",
            "rows": 4
        })
    )

    ns1 = forms.CharField(
        max_length=100,
        label="Primary Name Server (NS1)",
        initial="ns50.bisup.com",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "ns1.example.com"
        })
    )

    ns2 = forms.CharField(
        max_length=100,
        label="Secondary Name Server (NS2)",
        initial="ns51.bisup.com",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "ns2.example.com"
        })
    )


class BusinessDomainForm(forms.Form):

    representative_name = forms.CharField(
        max_length=100,
        label="Representative Name",
        initial="Sambhav Acharya",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "Authorized representative name"
        })
    )

    representative_email = forms.EmailField(
        label="Representative Email",
        widget=forms.EmailInput(attrs={
            "class": input_class,
            "placeholder": "Representative email"
        })
    )

    representative_phone = forms.CharField(
        max_length=20,
        label="Representative Phone",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "Representative phone number"
        })
    )

    company_name = forms.CharField(
        max_length=150,
        label="Company Name",
        initial="BISUP Innovations Pvt. Ltd.",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "Company name"
        })
    )

    company_registration_number = forms.CharField(
        max_length=100,
        label="Company Registration Number",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "Registration number"
        })
    )

    domain_name = forms.CharField(
        max_length=100,
        label="Domain Name",
        initial="bisup.com.np",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "example.com.np"
        })
    )

    business_description = forms.CharField(
        label="Business Description",
        initial="Hosting Provider",
        widget=forms.Textarea(attrs={
            "class": textarea_class,
            "placeholder": "Describe your business",
            "rows": 4
        })
    )

    ns1 = forms.CharField(
        max_length=100,
        label="Primary Name Server (NS1)",
        initial="ns50.bisup.com",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "ns1.example.com"
        })
    )

    ns2 = forms.CharField(
        max_length=100,
        label="Secondary Name Server (NS2)",
        initial="ns51.bisup.com",
        widget=forms.TextInput(attrs={
            "class": input_class,
            "placeholder": "ns2.example.com"
        })
    )