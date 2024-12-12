from django import template
register = template.Library()

@register.filter(name='word_count')
def word_count(value):
    """Кастомний фільтр: повертає кількість слів у тексті."""
    if not isinstance(value, str):
        return 0
    return len(value.split())


@register.simple_tag
def hello_text(name):
    return f"Hello, {name}!"
