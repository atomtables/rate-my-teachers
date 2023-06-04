from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=200)
    teachers = models.ManyToManyField('Teacher', blank=True, related_name='teachers')
    year_founded = models.IntegerField(blank=True)
    address = models.CharField(max_length=400, blank=True)
    principal = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    teaching = models.CharField(max_length=200, blank=True)
    classes = models.JSONField(blank=True, default=list)
    grades = models.JSONField(blank=True, default=list)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    overall_rating = models.FloatField(blank=True, default=5.0)
    comments = models.JSONField(blank=True, default=list)


@receiver(post_save, sender=Teacher)
def update_school_teachers(sender, instance, created, **kwargs):
    for x in School.objects.all():
        x.teachers.remove(instance)
    instance.school.teachers.add(instance)

