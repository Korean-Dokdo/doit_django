from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 정수 형태로 들어오는 url이라면 int 변수를 pk에 담아 blog/views의 single_post_page() 함수를 사용하라
    # path('<int:pk>', views.single_post_page),
    # path('', views.index),
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view())


]