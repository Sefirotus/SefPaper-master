from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

# Create your views here.
