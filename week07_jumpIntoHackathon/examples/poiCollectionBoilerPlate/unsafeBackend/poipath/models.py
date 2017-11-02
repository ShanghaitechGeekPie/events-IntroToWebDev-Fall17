from django.core.urlresolvers import reverse
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models


class poi(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    lat = models.FloatField()
    lng = models.FloatField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('poipath_poi_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('poipath_poi_update', args=(self.pk,))


class sns(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    api_root = models.URLField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('poipath_sns_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('poipath_sns_update', args=(self.pk,))


class extlnk(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    url = models.CharField(max_length=255)

    # Relationship Fields
    relsns = models.ForeignKey('poipath.sns', )
    relpoi = models.ForeignKey('poipath.poi', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('poipath_extlnk_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('poipath_extlnk_update', args=(self.pk,))


class tag(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    proposer = models.ManyToManyField(settings.AUTH_USER_MODEL, )
    relpoi = models.ManyToManyField('poipath.poi', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('poipath_tag_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('poipath_tag_update', args=(self.pk,))
