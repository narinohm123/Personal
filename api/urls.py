from django.urls import path 
from . import views
from .views import LoginView , UserView , LogoutView


urlpatterns = [
    path('', views.apiOverview, name="api-overview",),
    path('profile/', views.profile_con, name="profile",),
    path('user_Degree/', views.User_Degree_con, name="user_Degree",),
    path('Document/', views.Document_con, name="Document",),
    path('Event/', views.Event_con, name="Event",),
    path('Budget/', views.Budget_con, name="Budget",),
    path('Pending/', views.Pending_con, name="Pending",),
    path('Approval/', views.Approval_con, name="Approval",),
    path('login/', LoginView.as_view(), name="login",),
    path('user-profile/', UserView.as_view(), name="user-profile",),
    path('logout/', LogoutView.as_view(), name="logout",)
    

]
