from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
'''
@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	def __str__(self):
		return self.question_text

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    selected = models.BooleanField(default=0)
    def __str__(self):
    	return self.choice_text
'''