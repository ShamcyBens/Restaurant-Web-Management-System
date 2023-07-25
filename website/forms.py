from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.forms import widgets
from django import forms
from .models import Profile
# from .models import Room

# from .models import Profile


class RegistrationForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    

class ReservationForm(forms.Form):
    name = forms.CharField(max_length=100)
    phonenumber = forms.CharField(max_length=10)
    email = forms.EmailField()
    check_in_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

   
    # room_choices = Room.objects.all().values_list('id', 'room_name')
    room_capacity_choices = [(i, str(i)) for i in range(1, 11)]
    room_capacity = forms.ChoiceField(choices=room_capacity_choices)

    pricing_choices = [
        ('Single Room - ', 'Ksh.1000'),
        ('Bed sitter - ', 'Kshs.2000'),
        ('1 Bedroom - ', 'Kshs.3000'),
        ('Special Single Room - ', 'Ksh.4000'),
        ('Special Bed sitter - ', 'Kshs.5000'),
        ('Special 1 Bedroom - ', 'Kshs.6000'),
    ]
    room_pricing = forms.ChoiceField(choices=pricing_choices)
   
  
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio'] 


  
# class ProfileForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
    
    
# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class UpdateProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
#     bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

#     class Meta:
#         model = Profile
#         fields = ['avatar', 'bio']

