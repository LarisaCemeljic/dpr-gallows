from django.db import models

class Highscore(models.Model):
		 player_name = models.CharField(max_length=200)
		 highscore_date = models.DateTimeField('Highscore dete');
		 score = models.IntegerField(default=0)

class Word(models.Model):
		 word = models.CharField(max_length=200)