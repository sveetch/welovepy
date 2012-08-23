# -*- coding: utf-8 -*-
"""
Data models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from welovepy.utils.filefield import content_file_name

STRUCTURE_LOGO_UPLOADPATH = getattr(settings, 'STRUCTURE_LOGO_UPLOADPATH', 'accounts/userprofiles/logos/%Y/%m/%d')
STRUCTURE_LOGO_UPLOADTO = lambda instance,filename: content_file_name(STRUCTURE_LOGO_UPLOADPATH, instance, filename)

TOOL_PICTURE_UPLOADPATH = getattr(settings, 'TOOL_PICTURE_UPLOADPATH', 'alliance/tools/pictures/%Y/%m/%d')
TOOL_PICTURE_UPLOADTO = lambda instance,filename: content_file_name(TOOL_PICTURE_UPLOADPATH, instance, filename)

class Structure(models.Model):
    u"""
    Structure model
    """
    name = models.CharField(_('structure name'), unique=True, max_length=100, blank=False)
    website = models.CharField(_('website url'), blank=True, null=True, max_length=255)
    logo = models.ImageField(_('logo'), upload_to=STRUCTURE_LOGO_UPLOADTO, width_field="logo_width", height_field="logo_height", max_length=255, blank=True, null=True)
    logo_width = models.IntegerField(default=0)
    logo_height = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("structure")
        verbose_name_plural = _("structures")

class Skill(models.Model):
    """
    Skill
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    title = models.CharField(_('title'), unique=True, blank=False, max_length=255)
    description = models.TextField(_('description'), blank=False)
    visible = models.BooleanField(_('visibility'), default=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")


class Tool(models.Model):
    """
    Tool
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    title = models.CharField(_('title'), unique=True, blank=False, max_length=255)
    url = models.CharField(_('url'), blank=False, max_length=255)
    picture = models.ImageField(_('picture'), upload_to=TOOL_PICTURE_UPLOADTO, width_field="picture_width", height_field="picture_height", max_length=255, blank=True, null=True)
    picture_width = models.IntegerField(default=0)
    picture_height = models.IntegerField(default=0)
    description = models.TextField(_('description'), blank=False)
    visible = models.BooleanField(_('visibility'), default=True)
    suggest_from = models.ForeignKey(User, verbose_name=_('suggested by'), blank=True, null=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _("tool")
        verbose_name_plural = _("tools")
