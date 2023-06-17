from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from contact.models import Contact



class ContactForm(forms.ModelForm):
  picture = forms.ImageField(
    required=False,
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
    return email

class UserUpdateForm(forms.ModelForm):
  first_name = forms.CharField(
    min_length=3,
    max_length=30,
    help_text='Required.',
    required=True,
    error_messages={
      'min_length': 'Please, add more than 2 letters',
      'max_length': 'Please, add at most 30 letters',
      'required': 'This field is required'
    }
  )

  last_name = forms.CharField(
    min_length=3,
    max_length=30,
    help_text='Required.',
    required=True,
    error_messages={
      'min_length': 'Please, add more than 2 letters',
      'max_length': 'Please, add at most 30 letters',
      'required': 'This field is required'
    }
  )

  password = forms.CharField(
    label='Password',
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    help_text=password_validation.password_validators_help_text_html(),
    required=False
  )

  password_confirmation = forms.CharField(
    label='Password confirmation',
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    help_text='Use the same password as before.',
    required=False
  )

  class Meta:
    model = User
    fields = (
      'first_name',
      'last_name',
      'email',
      'username',
    )

  def save(self, commit=True):
    clean_data = self.cleaned_data
    user = super().save(commit=False)

    password = clean_data.get('password')

    if password:
      user.set_password(password)
    if commit:
      user.save()

    return user

  def clean(self):
    password = self.cleaned_data.get('password')
    password_confirmation = self.cleaned_data.get('password_confirmation')

    if password or password_confirmation:
      if password != password_confirmation:
        self.add_error(
          'password_confirmation',
          ValidationError(
            'Password must be the same'
          )
        )

    return super().clean()

  def clean_email(self):
    email = self.cleaned_data.get('email')
    current_email = self.instance.email

    if current_email != email:
      if User.objects.filter(email=email).exists():
        self.add_error(
          'email',
          ValidationError(
            'Email is already',
            code='invalid'
          )
        )
    return email

  def clean_password(self):
    password = self.cleaned_data.get('password')

    if password:
      try:
        password_validation.validate_password(password)
      except ValidationError as errors:
        self.add_error(
          'password',
          ValidationError(errors)
        )

    return password
