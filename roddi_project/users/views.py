from http.client import HTTPResponse

from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import CustomRegistrationForm, UserProfileUpdateForm, ImageUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, message=f'Account has been created! You can now login')
            return redirect('/../dashboard/')
    else:
        form = CustomRegistrationForm()
    return render(request=request, template_name='users/registration.html', context={'form': form})

@api_view(['GET'])
def notifyUser(request, email):
    try:
        user_obj = get_user_model()(email=email)
        message = render_to_string('estate/mail_template.html', {
            'user': user_obj.username,
        })
        send_mail('Røddi', message, None, [email], fail_silently=False,)
        return redirect('./')
    except:
        return HTTPResponse("Noe gikk galt, gå tilbake og prøv igjen")


class notify(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'users/notify.html'
    context_object_name = 'user_list'

    def test_func(self):
        return True

    # Her skal få alle tilhørene objekter.
    def get_context_data(self, *args, **kwargs):
        context = super(notify, self).get_context_data(
            *args, **kwargs)
        context['user_list'] = User.objects.all()
        return context


@login_required
def profile(request):
    # lage form
    return render(request=request, template_name='users/profile.html')


class update_profile(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = User
    template_name = 'users/update_profile.html'
    form_class = UserProfileUpdateForm
    second_form_class = ImageUpdateForm

    #hvor man returnerer etter opddatering
    def get_success_url(self):
        return reverse('profile')

    #denne trengs for å vite hvilken bruker som skal oppdate profil
    def get_object(self):
        return self.request.user

    #bare gyldig bruker kan akksessere denne siden
    def test_func(self):
        user = self.get_object()
        if (self.request.user == user):
            return True
        return False
        
    #setter variabelnavn
    def get_context_data(self, **kwargs):
        context = super(update_profile, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserProfileUpdateForm(request.POST, instance = request.user)
            form2 = ImageUpdateForm(request.POST, 
                                request.FILES, instance = request.user.profile)
            if form.is_valid() and form2.is_valid():
                form.save()
                return redirect('profile')
            else:
                form = UserProfileUpdateForm( instance = request.user)
                form2 = ImageUpdateForm(instance = request.user.profile) 
                
        context = {"form":form, "form2": form2}
        return render(request, "users/update_profile", context)