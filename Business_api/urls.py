from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# from rest_framework.routers import DefaultRouter
# from account.views import UserProfileViewset
# router = DefaultRouter()
# router.register(r'profile', UserProfileViewset, basename='userprofile')

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')), 
    path('api/card/', include('card.urls')), 
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
