from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from timeline import views


urlpatterns = [
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home.index, name='index'),
    url(r'^viewer/$', views.home.index_for_viewer, name='index_for_viewer'),
    url(r'^login/$', views.auth.log_in, name='log_in'),
    url(r'^auth/$', views.auth.authenticate, name='auth'),
    url(r'^logout/$', views.auth.logout, name='log_out'),
    url(r'^user/(?P<user_id>[0-9]+)$', views.viewer.account, name='account'),
    url(r'^add/$', views.work.add, name='add'),
    url(r'^editform/(?P<work_id>[0-9]+)/$', views.work.editform, name='editform'),
    url(r'^edit/$', views.work.edit, name='edit'),
    url(r'^delete/$', views.work.delete, name='delete'),
    url(r'^delete-each/(?P<work_id>[0-9]+)$', views.work.delete_each, name='delete_each'),
    url(r'^balance/$', views.home.balance, name='balance'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
