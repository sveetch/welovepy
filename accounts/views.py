# -*- coding: utf-8 -*-
"""
Accounts addtionnal views
"""
import datetime

from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from braces.views import UserFormKwargsMixin, LoginRequiredMixin

from sveeaccounts.views import MyAccountBaseView

from accounts.models import UserProfile

from accounts.forms import UserProfileForm

class MyAccountView(MyAccountBaseView):
    template_name = "accounts/user_form.html"
    form_class = UserProfileForm
    model = UserProfile
    
    def get_success_url(self):
        return reverse('accounts-my')
