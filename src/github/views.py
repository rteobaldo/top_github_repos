from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from github.models import ProgrammingLanguage, Repository


class RepositoryList(ListView):
    model = Repository
    template_name = 'repository_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        language_pk = self.kwargs.get('language_pk')
        return queryset.filter(language__pk=language_pk).order_by('-stargazers_count')


class RepositoryDetail(DetailView):
    model = Repository
    template_name = 'repository_details.html'


class ProgrammingLanguageCreate(CreateView):
    model = ProgrammingLanguage
    fields = ['name', ]
    template_name = 'form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programming_languages'] = ProgrammingLanguage.objects.all().order_by('name')
        return context
