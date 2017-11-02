from django.contrib import admin
from django import forms
from .models import poi, sns, extlnk, tag

class poiAdminForm(forms.ModelForm):

    class Meta:
        model = poi
        fields = '__all__'


class poiAdmin(admin.ModelAdmin):
    form = poiAdminForm
    list_display = ['name', 'created', 'last_updated', 'lat', 'lng']
    # readonly_fields = ['name', 'created', 'last_updated', 'lat', 'lng']

admin.site.register(poi, poiAdmin)


class snsAdminForm(forms.ModelForm):

    class Meta:
        model = sns
        fields = '__all__'


class snsAdmin(admin.ModelAdmin):
    form = snsAdminForm
    list_display = ['name', 'created', 'last_updated', 'api_root']
    # readonly_fields = ['name', 'created', 'last_updated', 'api_root']

admin.site.register(sns, snsAdmin)


class extlnkAdminForm(forms.ModelForm):

    class Meta:
        model = extlnk
        fields = '__all__'


class extlnkAdmin(admin.ModelAdmin):
    form = extlnkAdminForm
    list_display = ['created', 'last_updated', 'url']
    # readonly_fields = ['created', 'last_updated', 'url']

admin.site.register(extlnk, extlnkAdmin)


class tagAdminForm(forms.ModelForm):

    class Meta:
        model = tag
        fields = '__all__'


class tagAdmin(admin.ModelAdmin):
    form = tagAdminForm
    list_display = ['name', 'created', 'last_updated']
    # readonly_fields = ['name', 'created', 'last_updated']

admin.site.register(tag, tagAdmin)


