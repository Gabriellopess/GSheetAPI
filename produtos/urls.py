from django.urls import path
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('produto/list', view=views.ProdutoList.as_view(), name='produto-list'),
    path('produto/rud/<int:pk>', view=views.ProdutoRetrieveUpdateDestroy.as_view(), name='produto-rud')
]