# -*- coding: utf-8 -*-
"""
Forms
"""
from django import forms
from django.utils.translation import ugettext
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit
from crispy_forms.bootstrap import AppendedText

from alliance.models import Structure, Tool, Demand

class StructureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('user')
        
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.form_class = 'form-horizontal well'
        self.helper.form_style = 'inline'
        self.helper.add_input(Submit('submit', ugettext('Continue')))
        
        super(StructureForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Structure
        exclude = ('logo_width', 'logo_height')

class StructureSuggestForm(StructureForm):
    """
    Suggestion d'une nouvelle structure
    """
    def save(self, *args, **kwargs):
        instance = super(StructureSuggestForm, self).save(commit=False, *args, **kwargs)
        instance.suggest_from = self.author
        instance.save()
        return instance
    
    class Meta:
        model = Structure
        exclude = ('logo_width', 'logo_height', 'enabled', 'suggest_from')

class ToolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('user')
        
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.form_class = 'form-horizontal well'
        self.helper.form_style = 'inline'
        self.helper.add_input(Submit('submit', ugettext('Continue')))
        
        super(ToolForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Tool
        exclude = ('picture_width', 'picture_height')

class ToolSuggestForm(ToolForm):
    """
    Suggestion d'un nouvel outil
    """
    def save(self, *args, **kwargs):
        instance = super(ToolSuggestForm, self).save(commit=False, *args, **kwargs)
        instance.suggest_from = self.author
        instance.save()
        return instance
    
    class Meta:
        model = Tool
        exclude = ('picture_width', 'picture_height', 'enabled', 'suggest_from')

class DemandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.form_class = 'form-horizontal well'
        self.helper.form_style = 'inline'
        self.helper.add_input(Submit('submit', ugettext('Continue')))
        
        super(DemandForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Demand
        exclude = ('customer_care',)
