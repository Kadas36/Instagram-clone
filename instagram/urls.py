from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.insta_home, name='home'),
    path('profile/', views.new_post, name='newpost'),
    path('comment/<int:image_id>', views.Commentview, name='comment'),
    path( 'like/<int:pk>', views.Likeview, name='like_image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
