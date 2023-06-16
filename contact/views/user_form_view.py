from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import QueryDict
from typing import Union

from contact.forms import UserForm

def register(request):
  form = UserForm()

  if request.method == 'POST':
    form = UserForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, request.POST)
      return redirect('contact:index')


  return render(
    request,
    'contact/form_index.html',
    {
      'form': form,
      'title_form': 'Register',
    }
  )


def user_update(request, user_id):
  return render(
    request,
    'contact/form_index.html',
    {
      'title_form': 'Update user',
    }
  )


def login(request, request_login: Union[QueryDict, None] = None):
  form = AuthenticationForm(request)

  if request.method == 'POST':

    if request_login:
      keys = ['csrfmiddlewaretoken', 'username', 'password1']
      values = {key: request_login[key] for key in keys}
      values['password'] = values.pop('password1')
      form = AuthenticationForm(request, data=values)

    else:
      form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      user = form.get_user()
      auth.login(request, user)

  return render(
    request,
    'contact/form_index.html',
    {
      'form': form,
      'title_form': 'Login'
    }
  )

def logout(request):
  auth.logout(request)
  return redirect('contact:login')



# @Sambrano888
