from django.db import models


class Question(models.Model):
    class Meta:
        db_table = 'Question'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    question_text = models.CharField(max_length=200,verbose_name='Текст опроса')
    pub_date = models.DateTimeField('date published',auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    class Meta:
        db_table = 'Choice'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text