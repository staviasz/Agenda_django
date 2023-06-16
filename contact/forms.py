from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact



class ContactForm(forms.ModelForm):
  def __ini__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  class Meta:
    model = Contact
    fields = (
      'first_name',
      'last_name',
      'phone',
      'email',
      'description',
      'category',
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


