# -*- coding: utf-8 -*-
"""
Forms
"""
from django import forms
from django.utils.translation import ugettext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from crispy_forms.layout import Layout, Fieldset, Div
from crispy_forms.bootstrap import AppendedText

from sveeaccounts.forms import UserProfileBaseLayout, UserProfileBaseForm

from accounts.models import UserProfile

class AppendedLink(AppendedText):
    """
    Use the AppendedText element to put a link with an optionnal icon
    
    'icon' attribute in kwargs must be set to a valid named icon from 
    bootstrap (or your css theme if any).
    
    TODO: should not reside here, put it in a crispy fork ?
    """
    def __init__(self, field, link, text, *args, **kwargs):
        self.link = link
        self.icon = None
        if 'icon' in kwargs:
            self.icon = kwargs.pop('icon')

        super(AppendedLink, self).__init__(field, text, *args, **kwargs)

    def render(self, *args, **kwargs):
        content = self.text
        if self.icon is not None:
            content = u'<i class="{icon_name}"></i>'.format(icon_name=self.icon)
        self.text = u'<a href="{link}" title="{text}">{content}</a>'.format(link=self.link, content=content, text=self.text)
        return super(AppendedLink, self).render(*args, **kwargs)

def UserProfileLayout():
    """
    Return the default layout, this must be wrapped in a function to have 
    correct translations
    """
    return Layout(
        UserProfileBaseLayout(),
        Fieldset(
            ugettext('profile'),
            AppendedLink('structure', reverse("accounts-structure-suggest"), ugettext('add new'), icon="icon-plus"),
            'skills',
            AppendedLink('tools', reverse("accounts-tool-suggest"), ugettext('suggest a new tool'), icon="icon-plus-sign"),
        ),
    )
    
class UserProfileForm(UserProfileBaseForm):
    def __init__(self, *args, **kwargs):
        kwargs['layout'] = UserProfileLayout()
        super(UserProfileForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = UserProfile
        exclude = ('user', 'initiator')
