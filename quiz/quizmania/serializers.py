from quizmania.models import *
from rest_framework.serializers import ModelSerializer
from datetime import datetime

class QuizQuestionAddSerializer(ModelSerializer):
    class Meta:
        model = QuizCreation
        fields = '__all__'
    def create(self, validated_data): 
        start_date = validated_data.get('startDate') 
        end_date = validated_data.get('endDate') 
        current_date = datetime.now() 
        creation = QuizCreation.objects.create(**validated_data) 
        if start_date >= current_date: 
            updation = QuizCreation.objects.filter(id=creation.id).update( status='inactive' ) 
        if start_date <= current_date and end_date >= current_date: 
            updation = QuizCreation.objects.filter(id=creation.id).update( status='active' ) 
        validated_data['id'] = creation.id 
        return validated_data # return super().create(validated_data)
