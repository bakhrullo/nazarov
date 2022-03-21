from django.contrib import admin
from .models import *


class MarFileInline(admin.TabularInline):
    model = Maruza

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.binarytree_set.count()
        return extra


class MarAdmin(admin.ModelAdmin):
    inlines = [MarFileInline, ]


class AmaFileInline(admin.TabularInline):
    model = Amaliyot

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.binarytree_set.count()
        return extra


class AmaAdmin(admin.ModelAdmin):
    inlines = [AmaFileInline, ]


class MusFileInline(admin.TabularInline):
    model = MustaqilTalim

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.binarytree_set.count()
        return extra


class MusAdmin(admin.ModelAdmin):
    inlines = [MusFileInline, ]


class LabFileInline(admin.TabularInline):
    model = Labartoriya

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.binarytree_set.count()
        return extra


class LabAdmin(admin.ModelAdmin):
    inlines = [LabFileInline, ]


class ScopFileInline(admin.TabularInline):
    model = Scopus

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.binarytree_set.count()
        return extra


class ScopAdmin(admin.ModelAdmin):
    inlines = [ScopFileInline, ]


class OakFileInline(admin.TabularInline):
    model = OAK

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.binarytree_set.count()
        return extra


class OakAdmin(admin.ModelAdmin):
    inlines = [OakFileInline, ]


class KonfFileInline(admin.TabularInline):
    model = Konfirensiya

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.binarytree_set.count()
        return extra


class KonfAdmin(admin.ModelAdmin):
    inlines = [KonfFileInline, ]

admin.site.register(VisitNumber)
admin.site.register(ScopPage, ScopAdmin)
admin.site.register(KonfPage, KonfAdmin)
admin.site.register(AmaPage, AmaAdmin)
admin.site.register(OakPage, OakAdmin)
admin.site.register(LabPage, LabAdmin)
admin.site.register(MusPage, MusAdmin)
admin.site.register(MarPage, MarAdmin)
