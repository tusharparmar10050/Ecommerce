from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('' , views.home , name='home'),

    path('signup/', views.signup,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
