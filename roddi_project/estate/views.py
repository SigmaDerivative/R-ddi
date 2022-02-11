from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView

from .forms import CommentForm
from .models import Estate, Belongings, Comment
# from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class Dashboard(LoginRequiredMixin, ListView):
    model = Estate
    template_name = 'estate/dashboard.html'
    context_object_name = 'estate_list'

    class Meta:
        permissions = [
            ("view_estate", "Can view private estate")
        ]

    def get_queryset(self):
        return Estate.objects.filter(users=self.request.user)


class EstateDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Estate
    template_name = 'estate/estate_detail.html'
    context_object_name = 'estateDetail'

    def test_func(self):
        estate = self.get_object()
        current_user = self.request.user
        for estate in estate.users.all():
            if current_user == estate:
                return True
        return False

    # Her skal få alle tilhørene objekter.
    def get_context_data(self, *args, **kwargs):
        context = super(EstateDetailView, self).get_context_data(
            *args, **kwargs)
        context['belongings_list'] = Belongings.objects.all().filter(
            estate=self.object)
        context['comment_list'] = Comment.objects.all()

        return context


def homepage(request):
    return render(request=request, template_name='estate/homepage.html')
