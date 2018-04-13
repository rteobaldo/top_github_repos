from django.contrib import admin
from github.models import ProgrammingLanguage, Repository


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    pass
