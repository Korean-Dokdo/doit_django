from django.urls import path
from . import views

urlpatterns = [
    # 정수 형태로 들어오는 url이라면 int 변수를 pk에 담아 blog/views의 single_post_page() 함수를 사용하라
    # path('<int:pk>', views.single_post_page),
    # path('', views.index),
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),

]