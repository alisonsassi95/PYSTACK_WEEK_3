from django.contrib import admin
from django.urls import include, path
from autenticacao import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('sair/', views.sair, name="sair"),
]
