from django.urls import path
from . import views
from django.contrib.auth import views as authentificationViews
from .views import CreateMessage,MessageListView

urlpatterns = [
    # path('home', views.homePage, name='home'),
    path('home', MessageListView.as_view(), name='home'),
    path('', MessageListView.as_view(), name='home'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('loginPage',authentificationViews.LoginView.as_view(template_name='loginPage.html'),name='loginPage'),
    path('lgn',views.Login,name='login'),
    path('signup',views.Signup,name="signup"),
    path('logout',authentificationViews.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('post/new',CreateMessage.as_view(template_name='postMessage.html'),name='post'),
    path('chatRoom',views.chatRoomPage,name='chatRoom'),
    path('loadRoom',views.loadRoom,name='loadRoom'),
    path('<str:room>/',views.roomPage,name='room'),
    path('sendMessage',views.sendMessage,name='sendMessage'),
    path('takeMessages/<str:room>/', views.takeMessages, name="takeMessages")

    # path('room',views.roomPage,name='room')
]
