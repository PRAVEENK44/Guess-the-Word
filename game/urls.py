from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('game/', views.game_board, name='game_board'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('api/start-game/', views.start_new_game, name='start_new_game'),
    path('api/submit-guess/', views.submit_guess, name='submit_guess'),
    path('api/session/<int:session_id>/', views.get_session_data, name='get_session_data'),
]
