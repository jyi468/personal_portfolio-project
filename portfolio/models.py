from django.db import models
# If adding/editing model for DB
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')  # you can upload these photos to a location
    url = models.URLField(blank=True)  # can add blank as a property to anything

    # What shows in a project list on admin page
    def __str__(self):
        return self.title