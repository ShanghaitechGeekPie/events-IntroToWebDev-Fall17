import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import poi, sns, extlnk, tag
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_poi(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["lat"] = "lat"
    defaults["lng"] = "lng"
    defaults.update(**kwargs)
    return poi.objects.create(**defaults)


def create_sns(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["api_root"] = "api_root"
    defaults.update(**kwargs)
    return sns.objects.create(**defaults)


def create_extlnk(**kwargs):
    defaults = {}
    defaults["url"] = "url"
    defaults.update(**kwargs)
    if "relsns" not in defaults:
        defaults["relsns"] = create_sns()
    if "relpoi" not in defaults:
        defaults["relpoi"] = create_poi()
    return extlnk.objects.create(**defaults)


def create_tag(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "proposer" not in defaults:
        defaults["proposer"] = create_django_contrib_auth_models_user()
    if "relpoi" not in defaults:
        defaults["relpoi"] = create_poi()
    return tag.objects.create(**defaults)


class poiViewTest(unittest.TestCase):
    '''
    Tests for poi
    '''
    def setUp(self):
        self.client = Client()

    def test_list_poi(self):
        url = reverse('poipath_poi_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_poi(self):
        url = reverse('poipath_poi_create')
        data = {
            "name": "name",
            "lat": "lat",
            "lng": "lng",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_poi(self):
        poi = create_poi()
        url = reverse('poipath_poi_detail', args=[poi.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_poi(self):
        poi = create_poi()
        data = {
            "name": "name",
            "lat": "lat",
            "lng": "lng",
        }
        url = reverse('poipath_poi_update', args=[poi.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class snsViewTest(unittest.TestCase):
    '''
    Tests for sns
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sns(self):
        url = reverse('poipath_sns_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sns(self):
        url = reverse('poipath_sns_create')
        data = {
            "name": "name",
            "api_root": "api_root",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sns(self):
        sns = create_sns()
        url = reverse('poipath_sns_detail', args=[sns.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sns(self):
        sns = create_sns()
        data = {
            "name": "name",
            "api_root": "api_root",
        }
        url = reverse('poipath_sns_update', args=[sns.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class extlnkViewTest(unittest.TestCase):
    '''
    Tests for extlnk
    '''
    def setUp(self):
        self.client = Client()

    def test_list_extlnk(self):
        url = reverse('poipath_extlnk_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_extlnk(self):
        url = reverse('poipath_extlnk_create')
        data = {
            "url": "url",
            "relsns": create_sns().pk,
            "relpoi": create_poi().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_extlnk(self):
        extlnk = create_extlnk()
        url = reverse('poipath_extlnk_detail', args=[extlnk.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_extlnk(self):
        extlnk = create_extlnk()
        data = {
            "url": "url",
            "relsns": create_sns().pk,
            "relpoi": create_poi().pk,
        }
        url = reverse('poipath_extlnk_update', args=[extlnk.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class tagViewTest(unittest.TestCase):
    '''
    Tests for tag
    '''
    def setUp(self):
        self.client = Client()

    def test_list_tag(self):
        url = reverse('poipath_tag_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_tag(self):
        url = reverse('poipath_tag_create')
        data = {
            "name": "name",
            "proposer": create_django_contrib_auth_models_user().pk,
            "relpoi": create_poi().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_tag(self):
        tag = create_tag()
        url = reverse('poipath_tag_detail', args=[tag.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tag(self):
        tag = create_tag()
        data = {
            "name": "name",
            "proposer": create_django_contrib_auth_models_user().pk,
            "relpoi": create_poi().pk,
        }
        url = reverse('poipath_tag_update', args=[tag.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


