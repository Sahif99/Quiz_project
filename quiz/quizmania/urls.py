from django.urls import path 
from quizmania import views 
# from django.conf.urls import url, include 

# from rest_framework import routers # from rest_framework.authtoken import views as rest_framework_views 

urlpatterns = [ 
    path('quiz_question_add/', views.QuizQuestionAddView.as_view()),
    path('quiz_question_list/', views.QuizQuestionListView.as_view()), 
    path('quiz_question_right_answer/', views.QuizQuestionRightAnswerView.as_view()), 
    #CRON 
    path('quiz_status_auto_updatation/', views.QuizStatusAutoUpdationView.as_view()),
]