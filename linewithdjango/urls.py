from django.conf.urls import url

from .views import Ask

urlpatterns = [
    url('^ask/', Ask.as_view()),
]
