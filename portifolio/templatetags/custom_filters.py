from django import template

register = template.Library()

@register.filter
def get_count(queryset, language):
    return queryset.filter(name=language).first().project_count if queryset.filter(name=language).exists() else 0

@register.filter
def get_percentage(queryset, language):
    total_count = sum([item.project_count for item in queryset])
    language_count = queryset.filter(name=language).first().project_count if queryset.filter(name=language).exists() else 0
    return (language_count / total_count) * 100 if total_count > 0 else 0
