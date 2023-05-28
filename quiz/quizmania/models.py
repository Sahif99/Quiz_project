from django.db import models

# Create your models here.
class QuizCreation(models.Model):
    statusType = (
        ('active','active'),
        ('inactive','inactive'),
        ('finished','finished')
    )
    question = models.TextField(null=True,blank=True)
    options = models.JSONField()
    rightAnswer = models.IntegerField(null=True,blank=True)
    startDate = models.DateTimeField(null=True,blank=True)
    endDate = models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=25,choices=statusType,null=True,blank=True)
    class Meta:
        db_table =  'quiz_creation'
        