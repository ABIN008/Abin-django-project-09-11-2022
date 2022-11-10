
from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=150)
   
    def __str__(self):
        return (self.question)
        
class Choice(models.Model):
    choose=models.ForeignKey(Question,on_delete=models.CASCADE)
    Choice_1=models.CharField(max_length=150)
    Choice_2=models.CharField(max_length=150)
    Choice_3=models.CharField(max_length=150)
 
    def __str__(self):
        return (self.Choice_1)

    def __str__(self):
        return (self.Choice_2)

    def __str__(self):
        return (self.Choice_3)