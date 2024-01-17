from django import forms
from .models import Record
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), label="")
	first_name = forms.CharField(max_length=96, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), label="")
	last_name = forms.CharField(max_length=96, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), label="")

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password-confirm')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = 'password'
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password-confirm'].widget.attrs['class'] = 'form-control'
		self.fields['password-confirm'].widget.attrs['placeholder'] = 'Password'
		self.fields['password-confirm'].label = 'password-confirm'
		self.fields['password-confirm'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li></ul>'

		self.fields['password'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password'].label = ''
		self.fields['password'].help_text = '<p>Confirm yout password, Type the same password as before!</p>'

class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}), label="")
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder':'Email Address'}))
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Phone"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Address"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"City"}), label="")
	country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"State"}), label="")

	class Meta:
		model = Record
		exclude = ('user',)