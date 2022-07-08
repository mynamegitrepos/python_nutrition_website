from django.urls    import path
from . import views

# urlpatterns = lista ou array:
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar')
]