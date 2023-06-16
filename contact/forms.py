from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from contact.models import Contact



class ContactForm(forms.ModelForm):
  picture = forms.ImageField(
    widget = forms.FileInput()
  )
  class Meta:
    model = Contact
    fields = (
      'first_name',
      'last_name',
      'phone',
      'email',
      'description',
      'category',
      'picture',
    )

  def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name')

    if first_name.lower() == 'abc' or len(first_name) < 3:
      self.add_error(
      'first_name',
      ValidationError(
        'Invalid name',
        code='invalid'
        )
      )
    return first_name

class UserForm(UserCreationForm):
  first_name = forms.CharField(
    required=True,
    min_length=3
  )

  email = forms.EmailField()

  class Meta:
    model = User
    fields = (
      'first_name',
      'last_name',
      'email',
      'username',
      'password1',
      'password2',
    )

  def clean_email(self):
    email = self.cleaned_data.get('email')

    if User.objects.filter(email=email).exists():
      self.add_error(
        'email',
        ValidationError(
          'Email is already',
          code='invalid'
        )
      )
