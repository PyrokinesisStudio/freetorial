from django import template

from ..models import Category


register = template.Library()


@register.inclusion_tag('blog/category_widget.html')
def blog_category_widget():
    categories = Category.objects.all()
    return {
        'categories': categories,
    }
