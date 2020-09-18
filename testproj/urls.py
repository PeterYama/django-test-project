from django.contrib import admin
from django.urls import path
from pages.views import home_view, profile_view
from accounts.views import ProfileView


urlpatterns = [
    path('', home_view,name='home'),
    path('detail/', ProfileView.as_view(),name='detail'),
    path('profile/', profile_view,name='profile'),
    path('admin/', admin.site.urls),
]
