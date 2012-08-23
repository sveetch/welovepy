# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save as post_save_signal
from django.dispatch import receiver

from django.contrib.auth.models import User

from sveeaccounts.models import UserProfileBase, append_profile_on_user_create
from alliance.models import Structure, Skill, Tool

class UserProfile(UserProfileBase):
    u"""
    User Profile
    """
    initiator = models.ForeignKey(User, verbose_name=_('initiator'), related_name='profile_initiator', blank=True, null=True)
    structure = models.ForeignKey(Structure, verbose_name=_('structure'), blank=True, null=True)
    skills = models.ManyToManyField(Skill, verbose_name=_('skills'), blank=True)
    tools = models.ManyToManyField(Tool, verbose_name=_('tools'), limit_choices_to={'visible':True}, blank=True)


from functools import partial
signal_for_this_profile = partial(append_profile_on_user_create, extra_fields={
    #'structure_name': lambda i: i.username,
})
post_save_signal.connect(signal_for_this_profile, sender=User)
