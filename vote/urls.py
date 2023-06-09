"""vote URL Configuration

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

from polls.views import show_subjects, show_teachers
from polls import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_subjects),
    path('teachers/', show_teachers),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('login/', views.login),  # 加入登录页
    path('logout/', views.logout),  # 加入注销页
    path('captcha/', views.get_captcha),  # 验证码
    path('excel/', views.export_teachers_excel),
    path('pdf/', views.export_pdf),
    path('teachers_data/', views.get_teachers_data),  # echarts图表
    path('api/subjects/', views.show_subjects_api),  # 返回json数据
    path('index', views.show_index),
    path('echarts/', views.show_echarts),
    path('api/teachers/', views.teachers_api),
    path('restapi/subjects/', views.show_subjects_rest),
    path('subjects/', views.subjects_restapi),
    path('api/teachers_rest/', views.show_teachers_rest),
    # 获取Token的接口
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新Token有效期的接口
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证Token的有效性
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/sub_redis/', views.show_subjects_red),
]

