from django.shortcuts import render
from rest_framework import generics
from django.db import transaction
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime
from quizmania.models import *
from quizmania import serializers
from quiz.pagination import OnOffPagination
from custom_decorator import response_modify_decorator_list_or_get_after_execution_for_onoff_pagination 

# Create your views here.

class QuizQuestionAddView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = QuizCreation.objects.all()
    serializer_class = serializers.QuizQuestionAddSerializer
class QuizQuestionListView(APIView): 
    permission_classes = [AllowAny] 
    queryset = QuizCreation.objects.all().values() 
    pagination_class = OnOffPagination 
    def get_filter(self): 
        queryset = self.queryset
        status = self.request.query_params.get('status', None) 
        if status: 
            queryset=queryset.filter(status__iexact=status) 
        return queryset 
    @response_modify_decorator_list_or_get_after_execution_for_onoff_pagination 
    def get(self, request, *args, **kwargs): 
            # return Response1 
            count = self.request.query_params.get('count') 
            # Pagination Functionality 
            paginator = OnOffPagination() 
            page_size = self.request.GET['page_size'] 
            # Filter 
            self.queryset = self.get_filter() 
            if page_size == '0': 
                response = self.queryset 
                if count: 
                    count = len(response) 
                    return Response({'total_count': count}) 
            else:
                result_page = paginator.paginate_queryset(self.queryset, request) 
                response = paginator.get_paginated_response(result_page) 
                response = response.data 
                return Response(response) 
class QuizQuestionRightAnswerView(APIView): 
    permission_classes = [AllowAny] 
    queryset = QuizCreation.objects.all().values() 
    def get(self, request, *args, **kwargs): 
        question = self.request.query_params.get('question', None) 
        if question: 
            question_no = QuizCreation.objects.filter(id=question).first().options 
            for each in question_no.keys(): 
                if int(each)==QuizCreation.objects.filter(id=question).first().rightAnswer: 
                    answer = "The right answer is: " + question_no[each] 
                    return Response(answer) 
                # return super().get(request, *args, **kwargs) 
class QuizStatusAutoUpdationView(APIView): 
    # permission_classes = [PreSharedPermissionForQuiz] 
    permission_classes = [AllowAny,] 
    def get(self, request, *args, **kwargs): 
        try: 
            with transaction.atomic(): 
                current_datetime = datetime.now()
                all_quiz_list = list(QuizCreation.objects.values_list('id', flat=True)) 
                if all_quiz_list: 
                    for each_quiz in all_quiz_list: 
                        start_time_of_each_quiz = QuizCreation.objects.filter(id=each_quiz).first().startDate
                        end_time_of_each_quiz = QuizCreation.objects.filter(id=each_quiz).first().endDate 
                        if start_time_of_each_quiz <= current_datetime and end_time_of_each_quiz <= current_datetime: 
                            updation = QuizCreation.objects.filter(id=each_quiz).update( status='finished' ) 
                        if start_time_of_each_quiz >= current_datetime: 
                            updation = QuizCreation.objects.filter(id=each_quiz).update( status='inactive' ) 
                        if start_time_of_each_quiz <= current_datetime: 
                            if end_time_of_each_quiz >= current_datetime:
                                updation = QuizCreation.objects.filter(id=each_quiz).update( status='active' ) 
                    msg = "Updation Successful" 
                    return Response({'result':{"code":200,'result':msg}}) 
        except Exception as e: 
                raise e
        