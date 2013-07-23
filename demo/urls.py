from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': reverse_lazy('home'),
    }, name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
)
