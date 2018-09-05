from django.urls import re_path
from django.conf.urls import url, include

from rest_framework import routers

from apps.pessoas import views

app_name = 'pessoas'

router = routers.SimpleRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    re_path(
        r'^(?P<cpf>\d+)/$',
        views.PessoaRetrieveAPIView.as_view(),
        name='pessoa_informacoes'
    ),
]