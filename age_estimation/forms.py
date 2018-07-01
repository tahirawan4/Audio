from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms


class UserSignUpForm(UserCreationForm):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'gender', 'age', 'country']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password1'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password2'}))

    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    country = forms.CharField(max_length=50,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))

    # frequency1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # frequency2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # average = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # frequency1 = forms.CharField(widget=forms.HiddenInput())
    # frequency2 = forms.CharField(widget=forms.HiddenInput())
    # average = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        # self.fields['frequency'].widget.attrs['disabled'] = True
        # self.fields['frequency'].widget.attrs['required'] = True

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username already exist")
        return username

    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 18:
            raise forms.ValidationError("Age can't be more than 18.")
        return age


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254, label='UserName',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
