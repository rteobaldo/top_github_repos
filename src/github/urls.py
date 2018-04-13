from django.conf.urls import url
from django.urls import path

from github.views import ProgrammingLanguageCreate, RepositoryList, RepositoryDetail

urlpatterns = [
    path('<language_pk>/repositories/<pk>/', RepositoryDetail.as_view(), name='repository-detail'),
    path('<language_pk>/repositories/', RepositoryList.as_view(), name='repository-list'),
    path('', ProgrammingLanguageCreate.as_view(), name='programming-language-create'),
]
