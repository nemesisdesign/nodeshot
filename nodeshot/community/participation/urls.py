from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns


from nodeshot.community.participation import views


urlpatterns = patterns('nodeshot.community.participation.views',
    url(r'^/comments/add/$', views.CommentCreate.as_view()),
    url(r'^/comments/$', 'all_nodes_comments',name='api_all_nodes_comments'),
    url(r'^/participation/$','all_nodes_participation', name='api_all_nodes_participation'),
    url(r'^/nodes/(?P<slug>[-\w]+)/comments/$', 'node_comments',name='api_node_comments'),
    url(r'^/nodes/(?P<slug>[-\w]+)/ratings/$', 'node_ratings',name='api_ratings'),
    url(r'^/nodes/(?P<slug>[-\w]+)/participation/$', 'node_participation', name= 'api_node_participation'),
)

urlpatterns = format_suffix_patterns(urlpatterns)