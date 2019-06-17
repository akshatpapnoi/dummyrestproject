from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from api.views import *

app_name = 'api'

urlpatterns =[
    path('register/', ProfileCreateAPI.as_view(), name="register"),
    path('auth/token/', obtain_jwt_token),
    path('login/', LoginAPI.as_view(), name="login"),
    path('logout/', LogoutAPI.as_view(), name="logout"),
    path('retrieve/', ProfileRetrieveUpdateAPI.as_view(), name="retrieve"),
    path('profile-list/', ProfileListAPI.as_view(), name="profile-list"),
    path('add-friend/', AddFriendAPI.as_view(), name="add-friend"),
    path('remove-friend/', RemoveFriendAPI.as_view(), name="remove-friend"),

    
]
