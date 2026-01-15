from django.db import models

class StudentEnquiry(models.Model):
    COURSE_CHOICES = [
        ('python', 'Python Programming'),
        ('fullstack', 'Full Stack Development'),
        ('backend', 'Backend Development'),
        ('frontend', 'Frontend Development'),
        ('datascience', 'Data Science & AI/ML'),
    ]

    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    interested_course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
