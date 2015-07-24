from django.db import models

# Create your models here.

from bson import json_util
#from json import dumps
import json
import datetime

from django.db import models
from django.utils import timezone
from django.forms.models import model_to_dict


class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return json.dumps(model_to_dict(self),  default=json_util.default)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return json.dumps(model_to_dict(self),  default=json_util.default)