# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import *

# Register your models here.


class LinkInline(admin.TabularInline):
    model = Link
    extra = 3


class GalleryInline(admin.TabularInline):
    model = Project.gallery.through
    extra = 3


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (
        LinkInline,
        GalleryInline,
    )

    filter_horizontal = (
        'skill',
        'category',
        'organization'
    )

    list_filter = (
        'category',
        'organization',
        'location',
    )

    list_display = (
        'name',
        'headline',
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        # 'rating'
    )


# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     pass
