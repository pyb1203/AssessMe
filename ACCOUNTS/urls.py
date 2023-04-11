__author__ = 'Vishal'

from django.urls import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [###############Student url####################################
      re_path(r'^connection$', views.StudentFormView, name='loginform'),
      re_path(r'^logout/', views.logout, name='logout'),
      re_path(r'^$', views.Student_login, name='login'),
      re_path(r'^student_register$', views.student_register, name='student_register'),
      re_path(r'^student_home$', views.student_home, name='student_home'),
      re_path(r'^studentlist$', views.studentlist, name='studentlist'),
      re_path(r'^runcode$', views.run_code, name='studentlist'),
      re_path(r'^studentcourse/(?P<cid>([A-Za-z0-9]+))/$', views.student_course, name='student_course'),
      re_path(r'^viewassignment_student/(?P<asid>([A-Za-z0-9]+))/$', views.view_assignment_student,name='view_assignment_stud'),
      re_path(r'^viewquestion_student/(?P<aid_qid>([A-Za-z0-9_]+))/$', views.view_question_student,name='view_question'),
      re_path(r'^viewassignmentwisereport_student/(?P<aid>([A-Za-z0-9]+))/$', views.view_report_wise_student,name='view_assignmentwise_report'),
      re_path(r'^viewassignmentfullreport_student/(?P<cid>([A-Za-z0-9]+))/$', views.view_report_student,name='view_assignment_report'),
      re_path(r'^admin_login$', views.admin_login, name='admin_login'),
      re_path(r'^activation_page$', views.activation_page, name='activation_page'),
      re_path(r'password_reset',views.password_reset,name="password_reset"),


      ###################Professor URL#############################
      re_path(r'^professor_login$', views.professor_login, name='professor_login'),
      re_path(r'^professor_home$', views.professor_home, name='professor_home'),
      re_path(r'^professor_register$', views.professor_register, name='professor_register'),
      re_path(r'^professorlist$', views.professorlist, name='professorlist'),
      re_path(r'^question$', views.question, name='question'),
      re_path(r'^question/(?P<asid>([A-Za-z0-9]+))/$', views.question_as, name='question_as'),
      re_path(r'^questionbank$', views.questionbank, name='questionbank'),
      re_path(r'^createcourse$', views.createcourse, name='createcourse'),
      re_path(r'^courselist$', views.courselist, name='courselist'),
      re_path(r'^coursestudent/(?P<cid>([A-Za-z0-9]+))/$', views.course_student, name='coursestudent'),
      re_path(r'^courseta/(?P<cid>([A-Za-z0-9]+))/$', views.course_ta, name='courseta'),
      re_path(r'^createassignment/(?P<cid>([A-Za-z0-9]+))/$', views.createassignment, name='createassignment'),
      re_path(r'^createassignment_q/(?P<cid>([A-Za-z0-9]+))/$', views.createassignment_and_add_q,name='createassignmentwithq'),
      re_path(r'^assignmentlist$', views.assignmentlist, name='assignmentlist'),
      re_path(r'^professorcourse/(?P<cid>([A-Za-z0-9]+))/$', views.professor_course, name='professor_course'),
      re_path(r'^viewassignment/(?P<asid>([A-Za-z0-9]+))/$', views.view_assignment, name='view_assignmentprof'),
      re_path(r'^viewquestion/(?P<aid_qid>([A-Za-z0-9_]+))/$', views.view_question, name='view_question'),
      re_path(r'^viewsubmission/(?P<subid>([A-Za-z0-9]+))/$', views.view_submission,name='view_submissionprof'),
      re_path(r'^studentvsquestion_matrix/(?P<asid>([A-Za-z0-9]+))/$', views.studentvsques_matrix,name='view_studentvsquestion_matrix'),
      re_path(r'^professorcourse$', views.professor_course, name='professor_course'),

      ################Assistant Url################################
      re_path(r'^assistant_login$', views.Assistant_login, name='Assistant_login'),
      re_path(r'^assistant_register/(?P<cid>([A-Za-z0-9_]+))/$', views.assistant_register,name='assistant_register'),
      re_path(r'^assistantlist$', views.assistantlist, name='assistantlist'),
      re_path(r'^assistant_home$', views.assistant_home, name='assistant_home'),
      ############################################################
      # re_path(r'^assignment$' , views.assignment, name='assigment')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
