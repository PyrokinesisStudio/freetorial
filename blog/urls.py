from django.conf.urls import url

from .views import (CategoryListView,
                    CategoryDetailView,
                    PostListView,
                    PostDetailView) 


urlpatterns = [
    url(
        r'^categories/$',
        CategoryListView.as_view(),
        name='blog_category_list',
    ),
    url(
        r'^category/(?P<slug>[\w-]+)/$',
        CategoryDetailView.as_view(),
        name='blog_category_detail',
    ),
    url(
        r'^$',
        PostListView.as_view(),
        name='blog_post_list',
    ),
    url(
        r'^(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/(?P<slug>[\w-]+)/$',
        PostDetailView.as_view(),
        name='blog_post_detail',
    ),
]
