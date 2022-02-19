from django.urls import path, include
from . import adminViews, StaffViews,hodviews

from studmanagement import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('demo/', views.showDemopage),
    path('', views.showLoginpage),
    path('doLogin', views.doLogin),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('get_user_details', views.get_user_details, name="get_user_details"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('admin_home',adminViews.admin_home, name="admin_home"),
    path('staff_add/', adminViews.staff_add, name="staff_add"),
    path('add_staff_save', adminViews.staff_add_save, name="add_staff_save"),
    path('manage_staff/', adminViews.manage_staff, name="manage_staff"),
    path('delete_staff/<staff_id>/', adminViews.delete_staff, name="delete_staff"),

    path('hod_home',hodviews.hod_home, name="hod_home"),
    path('add_hod/', adminViews.add_hod, name="add_hod"),
    path('add_hod_save', adminViews.add_hod_save, name="add_hod_save"),
    path('manage_hod/', adminViews.manage_hod, name="manage_hod"),
    path('delete_hod/<hod_id>/', adminViews.delete_hod, name="delete_hod"),
   
    



    path('add_course/', adminViews.add_course, name="add_course"),
    path('add_course_save', adminViews.add_course_save, name="add_course_save"),
    path('manage_course/', adminViews.manage_course, name="manage_course"),
    path('delete_course/<course_id>/', adminViews.delete_course, name="delete_course"),



    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('add_student/', StaffViews.add_student, name="add_student"),
    path('manage_student/', StaffViews.manage_student, name="manage_student"),
    path('show_student', StaffViews.show_student, name="show_student"),

    path('result_home/', StaffViews.result_home, name="result_home"),
    path('add_result', StaffViews.add_result, name="add_result"),
    path('add_result_save', StaffViews.add_result_save, name="add_result_save"),
    path('manage_result/', StaffViews.manage_result, name="manage_result"),
    path('delete_result/<result_id>/', StaffViews.delete_result, name="delete_result"),

    path('resultana_home/', StaffViews.resultana_home, name="resultana_home"),
    path('add_ana/', StaffViews.add_ana, name="add_ana"),
    path('add_resultana_save', StaffViews.add_resultana_save, name="add_resultana_save"),
    path('man_resultana/', StaffViews.man_resultana, name="man_resultana"),
    path('del_resultana/<result_id>/', StaffViews.del_resultana, name="del_resultana"),

    path('add_student_save', StaffViews.add_student_save, name="add_student_save"),
    path('delete_student/<student_id>/', StaffViews.delete_student, name="delete_student"),
]

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
