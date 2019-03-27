  
from django.conf.urls import url
from app.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]