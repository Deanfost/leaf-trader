from django.conf.urls import patterns, url
from finpy import views

urlpatterns = patterns( "",
        url(r'^$', views.landing_page, name='landing_page'),
        url(r'^plotter/', views.plotter, name='plot'),
        url(r'^screener/', views.screener, name = "screener"),
        url(r'^login/',views.loggingIn, name = "loggingIn"),
        url(r'^pdfDownload/', views.pdfDownload, name = "pdfDownload"),
        url(r'^signup/',views.signup, name = "signup"),
        url(r'^altLogin/', views.altLogin, name = "altLogin"),
        url(r'^ajax/validate_username/', views.validate_username, name  = "validate_username"),
        url(r'^practiceAjax/', views.practiceAjax, name = "practiceAjax"),
        url(r'^loggingout/',views.loggingout, name = "loggingout"),
        url(r'^socialogin/',views.socialogin, name = "socialogin"),
        url(r'^practiceAjax/',views.practiceAjax, name = "practiceAjax"),





)
