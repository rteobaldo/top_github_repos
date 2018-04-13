from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from github.utils import get_github_repos


class ProgrammingLanguage(models.Model):

    name = models.CharField('Linguagem', max_length=256, unique=True)

    def __str__(self):
        return self.name


class Repository(models.Model):

    full_name = models.CharField('Nome', max_length=256)
    description = models.TextField('Descrição', blank=True, null=True)
    html_url = models.CharField('URL', max_length=256)
    stargazers_count = models.IntegerField('Stars')
    language = models.ForeignKey(ProgrammingLanguage, verbose_name="Linguagem",
                                 related_name="repositories", on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=ProgrammingLanguage)
def post_save_programming_language(sender, instance, created, **kwargs):
    repos = get_github_repos(instance.name)
    for repo in repos:
        Repository.objects.get_or_create(
            full_name=repo.get('full_name'),
            description=repo.get('description'),
            language=instance,
            html_url=repo.get('html_url'),
            stargazers_count=repo.get('stargazers_count'))
