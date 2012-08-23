# -*- coding: utf-8 -*-
"""
Homepage view
"""
import datetime

from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db.models import Count

from accounts.models import UserProfile
from alliance.models import Structure, Skill, Tool

class HomepageView(TemplateView):
    template_name = "homepage.html"
        
    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context.update({
            'skill_list': Skill.objects.all(),
            # Only display tools which have at less one member and are visible
            # HACK: Actually this is order on the picture attribute to separate item 
            #       with picture and item without in display, but this prevent to order 
            #       on title or member count
            'tool_list': Tool.objects.annotate(num_members=Count('userprofile')).filter(num_members__gte=1, visible=True).order_by('-picture'),
            # Only display structures which have at less one member and have a logo and website url
            # Contain a workaround for the null=True condition on Imagefields that are 
            # not really honored see https://code.djangoproject.com/ticket/10244
            'structure_list': Structure.objects.annotate(num_members=Count('userprofile')).filter(num_members__gte=1, website__isnull=False).exclude(logo=''), 
        })
        return context

class BatcaveIndex(TemplateView):
    # TODO: This will be the admin frontend, should be move to his own app
    template_name = "batcave_index.html"
