from django.contrib import admin
from django.urls import path
from pages.views import home_view, profile_view
from accounts.views import profile_detail_view


urlpatterns = [
    path('', home_view,name='home'),
    path('detail/', profile_detail_view,name='detail'),
    path('profile/', profile_view,name='profile'),
    path('admin/', admin.site.urls),
]
