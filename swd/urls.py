from django.conf.urls import include, url
from django.contrib import admin
#from tools import user
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

# REST
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    #REST
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    url(r'^', include('main.urls')),
 #   url(r'^create-users/', user.index, name='user'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
