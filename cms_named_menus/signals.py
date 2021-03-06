# -*- coding: utf-8 -*-
'''
Created on May 21, 2016

@author: jakob
'''
from cms_named_menus import cache
from cms_named_menus.models import CMSNamedMenu

from cms.models.titlemodels import Title
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=CMSNamedMenu, dispatch_uid='clear_cache_named_menu_saved')
def clear_cache_named_menu_saved(sender, instance, **kwargs):
    cache.delete(instance.name)
    
@receiver(post_delete, sender=CMSNamedMenu, dispatch_uid='clear_cache_named_menu_deleted')
def clear_cache_named_menu_deleted(sender, instance, **kwargs):
    cache.delete(instance.name)

@receiver(post_save, sender=Title, dispatch_uid='clear_cache_title_saved')
def clear_cache_title_saved(sender, instance, **kwargs):
    cache.delete_by_page_id(instance.page.id, instance.language)
    
@receiver(post_save, sender=Title, dispatch_uid='clear_cache_title_deleted')
def clear_cache_title_deleted(sender, instance, **kwargs):
    cache.delete_by_page_id(instance.page.id, instance.language)