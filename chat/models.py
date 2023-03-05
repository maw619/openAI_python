from django.db import models


class Chat(models.Model):
    prompt = models.TextField()
    answer = models.TextField()

    class Meta:
        managed = True
        db_table = 'chat'