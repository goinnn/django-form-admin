# Copyright (c) 2011-2013 by Yaco Sistemas <goinnn@gmail.com> or <pmartin@yaco.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.

try:
    from django.conf.urls import include, patterns, url
except ImportError:  # Django < 1.5
    from django.conf.urls.defaults import include, patterns, url

from django.contrib import admin
from django.views.generic import RedirectView

from .app.views import SendEmailView


admin.autodiscover()

js_info_dict = {
    'packages': ('django.conf',),
}

URL_SEND_EMAIL = '/admin/send-email/'

urlpatterns = patterns('',
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^$', RedirectView.as_view(url=URL_SEND_EMAIL), name='example_index'),
    url(r'^%s$' % URL_SEND_EMAIL[1:], SendEmailView.as_view(template_name='app/send_email.html'), name='app_send_email'),
    url(r'^admin/', include(admin.site.urls)),
)
