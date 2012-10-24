from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
	url(r'^$', 'principal.views.home'),
	url(r'^new/$','principal.views.new'),
	url(r'^proyectos/$','principal.views.lista_proyectos'),
	url(r'^privado/$','principal.views.privado'),
	url(r'^login/$','principal.views.login'),
	url(r'^logout/$','principal.views.logout'),

)
