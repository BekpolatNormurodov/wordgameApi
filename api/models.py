from django.db import models

class Hangman(models.Model):
    question = models.CharField(max_length=100, null=True)
    answer = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question[:10]