from __future__ import unicode_literals

from django.views.generic import DetailView, ListView, DateDetailView

from .models import Category, Post


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context.update({
            'object_list': Post.objects.published().filter(categories=context['object']),
        })
        return context


class PostListView(ListView):
    queryset = Post.objects.published()
    paginate_by = 1


class PostDetailView(DateDetailView):
    queryset = Post.objects.published()
    date_field = 'publish'
    month_format = '%m'
