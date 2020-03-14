"""django_restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api import views
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

schema_view=get_schema_view(title='API',renderer_classes=[OpenAPIRenderer,SwaggerUIRenderer])

router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api2/', include(('app02.urls', 'app02'), namespace='app02')),
    path('api3/',include(('app03.urls','app03'),namespace='app03')),
    path('api4/',include(('app04.urls','app04'),namespace='app04')),
    path('api5/',include(('app05.urls','app05'),namespace='app05')),
    path('api6/<str:version>/', include(('app06.urls', 'app06'), namespace='app06')),
    # path('api-token-auth/', obtain_auth_token),
    path('api-token-auth/', obtain_jwt_token),
    path('docs/', include_docs_urls(title='测试平台接口文档'))
]
