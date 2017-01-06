from django.db import models


class Highscore(models.Model):
    verbose_name = "Highscore"
    verbose_name_plural = "Highscores"
    player_name = models.CharField(max_length=200)
    highscore_date = models.DateTimeField('Highscore dete')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name


class Word(models.Model):
    verbose_name = "Word"
    verbose_name_plural = "Words"
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word
