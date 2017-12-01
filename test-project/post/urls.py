from django.conf.urls import url

from post import views


urlpatterns = (
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post'),
    url(r'^post/(?P<pk>[0-9]+)/like/$', views.LikeState.as_view(),
        name='like'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.CreateComment.as_view(),
        name='comment'),
    url(r'^post/make/$', views.CreatePost.as_view(), name='make'),
    url(r'^$', views.PostList.as_view(), name='list')
)
