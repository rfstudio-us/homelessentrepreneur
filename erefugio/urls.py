"""erefugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^facilities/',views.all_data),

    url(r'^api/fac', views.All_Facilities_API.as_view(), name='faclist'),
    url(r'^api/userall', views.All_user_API.as_view(), name='users_all'),
    url(r'^api/homeless', views.All_homeless_API.as_view(), name='homel'),
    url(r'^api/user/',views.get_user_profile.as_view()),
    url(r'^api/profile/(?P<pk>[0-9]+)/$',views.Profile_API.as_view()),
    url(r'^api/User/',views.get_user_details.as_view()),
    url(r'^api/job/',views.JobList.as_view()),
    url(r'^api/facput/',views.Facility_API.as_view()),
    url(r'^api/facpost/',views.FacilitiesList.as_view()),
    url(r'^api/shortsurvey/',views.ShortSurveyList.as_view()),]



urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.jwt')),
]
