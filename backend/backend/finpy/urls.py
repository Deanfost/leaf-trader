from django.conf.urls import patterns, url
from finpy import views

urlpatterns = patterns( "",
        url(r'^$', views.landing_page, name='landing_page'),
        url(r'^plotter/', views.plotter, name='plot'),
        url(r'^screener/', views.screener, name = "screener"),
        url(r'^screener2/', views.screener2, name = "screener2"),

)
