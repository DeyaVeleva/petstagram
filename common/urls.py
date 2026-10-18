from django.urls import path,include
from common import views

app_name = 'common'
urlpatterns = [
    path('', views.home_page_view, name='home_page'),
    path('like/<int:photo_id>/', views.like_photo, name='like'),
    path('share/<int:photo_pk>/', views.share_photo, name='share'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment'),
]