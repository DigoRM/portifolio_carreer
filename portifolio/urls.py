from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView



urlpatterns = [

    path('register/', views.register, name='register'),
    path('accounts/login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile' ),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),

    path("", views.home, name='home'),
    path("categories/", views.categories, name='categories'),
    path("project/<int:pk>/detail", views.project_detail, name='project_detail'),
    path("category/<int:pk>/projects", views.category_projects, name='category_projects'),
    path('projects/language/<str:language>/', views.projects_language, name='projects_language'),
    path('projects/framework/<str:framework>/', views.projects_framework, name='projects_framework'),
    path('update/project/<int:pk>/', views.new_update, name='new_update'),

    # Courses
    path("courses/", views.courses, name='courses'),
    path("course/<int:pk>/detail", views.course_detail, name='course_detail'),
    path("category/<int:pk>/courses", views.category_courses, name='category_courses'),
    path('courses/language/<str:language>/', views.courses_language, name='courses_language'),
    path('courses/framework/<str:framework>/', views.courses_framework, name='courses_framework'),

    path('search/', views.search, name='search'),
    path('metrics/frameworks/<str:language>/', views.framework_progress_language, name='framework_progress_language'),
    path('metrics/frameworks/<int:pk>/', views.framework_progress_category, name='framework_progress_category'),
    path('metrics/<int:pk>/frameworks/', views.framework_progress_category2, name='framework_progress_category2'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)