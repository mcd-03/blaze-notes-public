import datetime
from django.db import models
from django.contrib.auth.models import User
from review.models import Topic, M1_Topic, M12_Topic, M23_Topic

courses = [
    ("M1", "Math 1"),
	("M1/2", "Math 1/2"),
	("M2/3", "Math 2/3"),
]

teachers = [
    ("Reckerd", "Reckerd"),
    ("Adnan", "Adnan"),
    ("Pait", "Pait"),
    ("Roberts", "Roberts"),
    ("Musick", "Musick"),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.CharField(max_length=30, choices=teachers, default="Roberts")
    course = models.CharField(max_length=10, choices=courses, default="M1")
    streak = models.PositiveSmallIntegerField(default=1)
    reference_date = models.DateField(default=datetime.date.today)
    login_count = models.PositiveSmallIntegerField(default=1)
    
    def __str__(self):
        return f'{self.user.username} Profile'
        
    def update_streak(self):
        # retrieving attributes for current user to use with next logic blocks
        last_active = self.reference_date
        today = datetime.date.today()
        difference = today - last_active

        # adds one to the login count if the last login was not today
        if last_active != today:
            temp = self.login_count
            self.login_count = temp + 1
            self.save()
            
        # checks if streak should be updated, then updates user streak
        if difference.days == 1:
            temp = self.streak
            self.streak = temp + 1
            self.save()
        elif last_active == today:
            pass
        else:
            self.streak = 1
            self.save()
        self.reference_date = today
        self.save()

    def create_review_list(self):
        #find the course of the user
        course = self.course

        #dictionary to reference the correct Topic model by course
        course_reference = {
            "M1": M1_Topic,
            "M1/2": M12_Topic,
            "M2/3": M23_Topic,
        }

        """ creates the list of topics to send with the view
        sends all topics that have been taught so that the
        the links to old materials can be accessed """
        focused_topics = course_reference[course].objects.filter(topic_date__lte = datetime.date.today())
        topics = [t for t in focused_topics]
        context = {'topics': topics}
        context['title'] = "Today's Topics"

        none_today = not any(map(Topic.time_to_review, topics))

        if none_today:
            context['nothing_today'] = 'Nothing to review today!'

        return context
    
