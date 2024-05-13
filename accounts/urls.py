from django.urls import path
from . import views
# from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [

    path('register/',views.UserRegister.as_view()),
    # path('api-token-auth/',auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


router = routers.SimpleRouter()
router.register('user',views.UserViewSet)

urlpatterns += router.urls


# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNTcyNTY3MiwiaWF0IjoxNzE1NjM5MjcyLCJqdGkiOiI4NTY4M2ZmZTMxMzg0MjQxODM1NjA5OTZmMDJiMjI1NiIsInVzZXJfaWQiOjF9.6GFXNQeZQ-PoagRTirmpozepKRGd9daxBwV4oIThZAU",
# }