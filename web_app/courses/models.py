from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.TextField()
    TYPES = [('P', 'Paid'), ('F', 'Free')]
    free_or_paid = models.CharField(choices=TYPES, max_length=1, blank=True)
    rate = models.IntegerField(default=0)
    text = models.TextField(blank=True)
    instructor_rate = models.IntegerField(default=0)
    pace_rate = models.IntegerField(default=0)
    depth_coverage_rate = models.IntegerField(default=0)
    quality_rate = models.IntegerField(default=0)
    number_of_comments = models.PositiveIntegerField(default=0)
    number_of_views = models.PositiveIntegerField(default=0)
    media_url = models.URLField(blank=True, null=True)
    medium = models.CharField(max_length=100)
    excersice = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Comment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey("Comment", on_delete=models.CASCADE, blank=True, null=True)
    rate = models.IntegerField(default=0)
    text = models.TextField()
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)

