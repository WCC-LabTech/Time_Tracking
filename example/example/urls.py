from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('example.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('scheducal.urls')),
    url(r'payperiod/^', include('pay_period.urls')),
    url(r'^auth/', include('tokenauth.urls')),
<<<<<<< HEAD
    url(r'^request/', include('faculty_request.urls')),
    url(r'^inventory/', include('Inventory_Management.urls')),
=======
>>>>>>> a40e9142b4d258d8db66c5ca208cf6e3eec12544
)
