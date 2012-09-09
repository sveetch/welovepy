# -*- coding: utf-8 -*-
"""
Accounts addtionnal views
"""
import datetime

from django.utils.translation import ugettext
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages

from braces.views import UserFormKwargsMixin, LoginRequiredMixin, SuccessURLRedirectListMixin

from alliance.models import Structure, Tool, Demand

from alliance.forms import StructureForm, ToolForm, ToolSuggestForm, DemandForm

class StructureCreateBaseView(LoginRequiredMixin, UserFormKwargsMixin, SuccessURLRedirectListMixin, CreateView):
    template_name = "alliance/structure_form.html"
    form_class = StructureForm
    model = Structure

class MyStructureCreateView(StructureCreateBaseView):
    """
    TODO: This should work like "MyToolCreateView" with a suggest form, not a direct create
    """
    def form_valid(self, form):
        resp = super(MyStructureCreateView, self).form_valid(form)
        messages.success(self.request, ugettext('Your suggested structure "%(structure)s" has been successfully registred, a moderator has to edit it to be available') % {'structure': self.object.name})
        return resp

class ToolCreateBaseView(LoginRequiredMixin, UserFormKwargsMixin, SuccessURLRedirectListMixin, CreateView):
    template_name = "alliance/tool_form.html"
    form_class = ToolForm
    model = Tool

class MyToolCreateView(ToolCreateBaseView):
    form_class = ToolSuggestForm
    
    def form_valid(self, form):
        resp = super(MyToolCreateView, self).form_valid(form)
        messages.success(self.request, ugettext('Your suggested tool "%(tool_name)s" has been successly registred, a moderator has to edit it to be available') % {'tool_name': self.object.title})
        return resp

class DemandCreateView(SuccessURLRedirectListMixin, CreateView):
    template_name = "alliance/demand_form.html"
    form_class = DemandForm
    model = Demand
    
    def get_success_url(self):
        return reverse('demand-public-add')
    
    def form_valid(self, form):
        resp = super(DemandCreateView, self).form_valid(form)
        messages.success(self.request, ugettext('Your demand has been saved, we will contact you soon'))
        return resp
