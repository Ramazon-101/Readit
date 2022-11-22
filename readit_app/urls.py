from django.urls import path, include
from .views import home_view, article_list, article_detail

app_name = 'readit'

urlpatterns = [
    path('', home_view, name='home_view'),
    path('blog/', article_list, name='article_list'),
    path('detail/<slug:slug>/', article_detail, name='article_detail'),
    path('api/', include('readit_app.api.urls'))
]
