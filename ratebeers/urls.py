from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'ratebeers.beers.views.home', name='home'),
    url(r'^like/(?P<beer_slug>.*)$', 'ratebeers.beers.views.like', name='like'),
    url(r'^dislike/(?P<beer_slug>.*)$', 'ratebeers.beers.views.dislike', name='dislike'),
    url(r'^ajax/like/(?P<beer_slug>.*)$', 'ratebeers.beers.views.ajax_like', name='ajax_like'),
    url(r'^ajax/dislike/(?P<beer_slug>.*)$', 'ratebeers.beers.views.ajax_dislike', name='ajax_dislike'),
    url(r'^(?P<beer_slug>.*)$', 'ratebeers.beers.views.individual_beer', name='individual_beer'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
