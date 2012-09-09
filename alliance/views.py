# -*- coding: utf-8 -*-
"""
Accounts addtionnal views
"""
import datetime

from django.utils.translation import ugettext
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages

from braces.views import UserFormKwargsMixin, LoginRequiredMixin, StaffuserRequiredMixin, SuccessURLRedirectListMixin, ListAppendView

from alliance.models import Structure, Tool, Demand

from alliance.forms import StructureForm, StructureSuggestForm, ToolForm, ToolSuggestForm, DemandForm

class StructureCreateBaseView(LoginRequiredMixin, UserFormKwargsMixin, SuccessURLRedirectListMixin, CreateView):
    template_name = "alliance/structure_form.html"
    form_class = StructureForm
    model = Structure

class StructureSuggestView(StructureCreateBaseView):
    form_class = StructureSuggestForm
    
    def form_valid(self, form):
        resp = super(StructureSuggestView, self).form_valid(form)
        messages.success(self.request, ugettext('Your suggested structure "%(structure)s" has been successfully registred, a moderator has to edit it to be available') % {'structure': self.object.name})
        return resp

class ToolCreateBaseView(LoginRequiredMixin, UserFormKwargsMixin, SuccessURLRedirectListMixin, CreateView):
    template_name = "alliance/tool_form.html"
    form_class = ToolForm
    model = Tool

class ToolSuggestView(ToolCreateBaseView):
    form_class = ToolSuggestForm
    
    def form_valid(self, form):
        resp = super(ToolSuggestView, self).form_valid(form)
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

class BatcaveIndex(StaffuserRequiredMixin, TemplateView):
    template_name = "alliance/batcave-index.html"
        
    def get_context_data(self, **kwargs):
        context = super(BatcaveIndex, self).get_context_data(**kwargs)
        context.update({
            'member_count': User.objects.filter(is_superuser=False).count(),
            'pending_demands': Demand.objects.filter(customer_care__isnull=True).order_by('-created'), 
            'pending_structures': Structure.objects.filter(enabled=False).order_by('-created'), 
            'pending_tools': Tool.objects.filter(enabled=False).exclude(suggest_from__isnull=True).order_by('-created'),
        })
        return context

class BatcaveStructureList(StaffuserRequiredMixin, UserFormKwargsMixin, ListAppendView):
    model = Structure
    form_class = StructureForm
    template_name = "alliance/batcave-structure-list.html"
    paginate_by = 25
