
from django.conf.urls import url
from . import views

urlpatterns = [
    # # path('db', views.putindb, name='putindb'),
    # # path('', views.forum, name='forum'),
    # url(r'^forumpage/(?P<roomID>.+)/',views.homepage, name='homepage'),
    # url(r'^forumpage/',views.homepageRedirect, name='homepageRedirect'),
    # url(r'^db',views.get_post_list.as_view(), name='indb'),
    url(r'^grid', views.canvas.as_view(), name='grid'),
    url(r'^homepage', views.homepage, name='homepage'),
    url(r'^draw', views.draw, name='draw'),
    url(r'^update', views.update.as_view(), name='update'),
]




