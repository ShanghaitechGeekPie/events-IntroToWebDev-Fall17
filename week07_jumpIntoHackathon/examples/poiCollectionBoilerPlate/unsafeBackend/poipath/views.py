from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import poi, sns, extlnk, tag
from .forms import poiForm, snsForm, extlnkForm, tagForm


class poiListView(ListView):
    model = poi


class poiCreateView(CreateView):
    model = poi
    form_class = poiForm


class poiDetailView(DetailView):
    model = poi


class poiUpdateView(UpdateView):
    model = poi
    form_class = poiForm


class snsListView(ListView):
    model = sns


class snsCreateView(CreateView):
    model = sns
    form_class = snsForm


class snsDetailView(DetailView):
    model = sns


class snsUpdateView(UpdateView):
    model = sns
    form_class = snsForm


class extlnkListView(ListView):
    model = extlnk


class extlnkCreateView(CreateView):
    model = extlnk
    form_class = extlnkForm


class extlnkDetailView(DetailView):
    model = extlnk


class extlnkUpdateView(UpdateView):
    model = extlnk
    form_class = extlnkForm


class tagListView(ListView):
    model = tag


class tagCreateView(CreateView):
    model = tag
    form_class = tagForm


class tagDetailView(DetailView):
    model = tag


class tagUpdateView(UpdateView):
    model = tag
    form_class = tagForm

