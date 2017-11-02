from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'poi', api.poiViewSet)
router.register(r'sns', api.snsViewSet)
router.register(r'extlnk', api.extlnkViewSet)
router.register(r'tag', api.tagViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for poi
    url(r'^poipath/poi/$', views.poiListView.as_view(), name='poipath_poi_list'),
    url(r'^poipath/poi/create/$', views.poiCreateView.as_view(), name='poipath_poi_create'),
    url(r'^poipath/poi/detail/(?P<pk>\S+)/$', views.poiDetailView.as_view(), name='poipath_poi_detail'),
    url(r'^poipath/poi/update/(?P<pk>\S+)/$', views.poiUpdateView.as_view(), name='poipath_poi_update'),
)

urlpatterns += (
    # urls for sns
    url(r'^poipath/sns/$', views.snsListView.as_view(), name='poipath_sns_list'),
    url(r'^poipath/sns/create/$', views.snsCreateView.as_view(), name='poipath_sns_create'),
    url(r'^poipath/sns/detail/(?P<pk>\S+)/$', views.snsDetailView.as_view(), name='poipath_sns_detail'),
    url(r'^poipath/sns/update/(?P<pk>\S+)/$', views.snsUpdateView.as_view(), name='poipath_sns_update'),
)

urlpatterns += (
    # urls for extlnk
    url(r'^poipath/extlnk/$', views.extlnkListView.as_view(), name='poipath_extlnk_list'),
    url(r'^poipath/extlnk/create/$', views.extlnkCreateView.as_view(), name='poipath_extlnk_create'),
    url(r'^poipath/extlnk/detail/(?P<pk>\S+)/$', views.extlnkDetailView.as_view(), name='poipath_extlnk_detail'),
    url(r'^poipath/extlnk/update/(?P<pk>\S+)/$', views.extlnkUpdateView.as_view(), name='poipath_extlnk_update'),
)

urlpatterns += (
    # urls for tag
    url(r'^poipath/tag/$', views.tagListView.as_view(), name='poipath_tag_list'),
    url(r'^poipath/tag/create/$', views.tagCreateView.as_view(), name='poipath_tag_create'),
    url(r'^poipath/tag/detail/(?P<pk>\S+)/$', views.tagDetailView.as_view(), name='poipath_tag_detail'),
    url(r'^poipath/tag/update/(?P<pk>\S+)/$', views.tagUpdateView.as_view(), name='poipath_tag_update'),
)

