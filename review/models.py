from django.db import models
import datetime

courses = [
    ("M1", "Math 1"),
	("M1/2", "Math 1/2"),
	("M2/3", "Math 2/3"),
]

class Topic(models.Model):
	topic_name = models.CharField(max_length=200)
	topic_date = models.DateField('date taught')
	topic_img = models.ImageField()
	topic_key = models.ImageField()

	class Meta:
		abstract = True

	def __str__(self):
		return self.topic_name

	def time_to_review(self):
		days_ago = datetime.date.today() - self.topic_date
		if days_ago.days in [0, 1, 3, 5, 8, 13, 21, 34, 55, 89, 144]:
			return 1
		else: return 0

	def already_taught(self):
		if self.topic_date <= datetime.date.today():
			return 1
		else: return 0

class M1_Topic(Topic):
    class Meta:
        abstract = False
        ordering = ['topic_date']

class M12_Topic(Topic):
    class Meta:
        abstract = False
        ordering = ['topic_date']

class M23_Topic(Topic):
    class Meta:
        abstract = False
        ordering = ['topic_date']