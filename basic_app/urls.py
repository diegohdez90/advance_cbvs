from django.conf.urls import url
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
  url(r'^$', views.SchollListView.as_view(), name="list"),
  url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(),name='detail')
]