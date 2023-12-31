from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


def create(request):
  form_action = reverse('contact:create')
  if request.method == 'GET':
    context = {
      'form': ContactForm(),
      'form_action': form_action,
      'title_form': 'Create Contact'
    }
  else:
    form = ContactForm(request.POST, request.FILES)
    context = {
      'form': form,
      'form_action': form_action,
      'title_form': 'Create Contact'
    }

    if form.is_valid():
      contact = form.save(commit=False)
      contact.owner = request.user
      contact.save()
      return redirect('contact:update', contact_id=contact.pk)

  return render(request, 'contact/form_index.html', context)

def update(request, contact_id):
  contact = get_object_or_404(
    Contact,
    pk=contact_id,
    show=True,
    owner=request.user
  )
  form_action = reverse('contact:update', args=(contact_id,))

  if request.method == 'GET':
    context = {
      'form': ContactForm(instance=contact),
      'form_action': form_action,
      'title_form': 'Update Contact'
    }
  else:
    form = ContactForm(request.POST,request.FILES , instance=contact)
    context = {
      'form': form,
      'form_action': form_action,
      'title_form': 'Update Contact'
    }

    if form.is_valid():
      contact = form.save()
      return redirect('contact:update', contact_id=contact.pk)

  return render(request, 'contact/form_index.html', context)

def delete(request, contact_id):
  contact = get_object_or_404(
    Contact,
    pk=contact_id,
    show=True,
    owner=request.user
  )

  confirmation = request.POST.get('confirmation', 'no')

  if confirmation == 'yes':
    contact.delete()
    return redirect('contact:index')

  return render(request,
                'contact/contact.html',
                {
                  'contact': contact,
                  'confirmation': confirmation
                })
