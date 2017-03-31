from django.conf.urls import url
# from .views import post_list
# from .views import PostList, PostDetail, CreateComment
# can also be imported as below
from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name="post-list"),
    # url(r'^$', post_list),
    url(r'^(?P<pk>[0-9])/$', views.PostDetail.as_view(), name="post-detail"),
    url(r'^(?P<pk>[0-9])/comment/$', views.CreateComment.as_view(), name="create-comment"),
]
