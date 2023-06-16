from django.shortcuts import render
from contact.forms import UserForm

def register(request):
  form = UserForm()

  if request.method == 'POST':
    form = UserForm(request.POST)

    if form.is_valid():
      form.save()

  return render(
    request,
    'contact/register.html',
    {
      'form': form,
    }
  )
