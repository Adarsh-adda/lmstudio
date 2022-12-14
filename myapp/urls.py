from django.urls import path
from .views import (
    Home,
    PostListView,
    PostDetailView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('blog/<int:pk>/<slug:slug>/',
         PostDetailView.as_view(), name='blog-detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)