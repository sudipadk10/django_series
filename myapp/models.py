# This file defines the data models for your app.
# Models are Python classes that map to database tables.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  # First name of the student
    email = models.EmailField(unique=True)  # Email (must be unique)
    age = models.IntegerField()  # Age of the student
    enrollment_date = models.DateTimeField(auto_now_add=True)  # Timestamp (when student was added)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # String representation
