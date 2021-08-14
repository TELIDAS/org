from django.db import models

from npo_user.models import NPOUser


class Question(models.Model):
    user = models.ForeignKey(NPOUser,
                             on_delete=models.CASCADE,
                             related_name='user_questions',
                             null=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'

    def filter(self):
        return AdminAnswer.objects.filter(text=self)


class AdminAnswer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='admin_answer',
                                 null=True)

    def __str__(self):
        return f'{self.text}'
