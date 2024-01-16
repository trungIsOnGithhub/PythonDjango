class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=96, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=96, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}), label="")
	email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={"class":"form-control", 'placeholder':'Email Address'}))
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Phone"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Address"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"City"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"State"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"Zipcode"}), label="")

	class Meta:
		model = Record
		exclude = ("user")