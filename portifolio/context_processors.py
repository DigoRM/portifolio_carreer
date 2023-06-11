from .models import Category, Framework, ProgrammingLanguage
from django.db.models import Count


def all_categories_context(request):
    all_categories = Category.objects.annotate(num_projects=Count('projects')).order_by('-num_projects')
    return {'all_categories': all_categories}

def all_languages_context(request):
    all_languages = ProgrammingLanguage.objects.annotate(num_language=Count('id')).order_by('-num_language')
    return {'all_languages': all_languages}

def all_frameworks_context(request):
    all_frameworks = Framework.objects.annotate(num_frameworks=Count('id')).order_by('-num_frameworks')
    return {'all_frameworks': all_frameworks}

