from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'free_or_paid', 'rate', 'text', 'instructor_rate', 'pace_rate', 'depth_coverage_rate',
                    'quality_rate', 'number_of_comments', 'number_of_views', 'media_url', 'have_book', 'have_excersice',
                    'have_site', 'have_video', 'submitter']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'parent', 'rate', 'text', 'submitter']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
