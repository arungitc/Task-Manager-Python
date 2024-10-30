from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Report(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, blank=True)
    date = models.DateField(blank=True, null=True)
    subject = models.TextField(max_length=240, blank=True)
    docId = models.CharField(max_length=100, blank=True)
    head_under_project_website = models.TextField(max_length=50, blank=True)
    
    pdf_link = models.URLField(max_length=200, blank=True)
    other_pdf = models.URLField(max_length=200, blank=True)

    STATUS_CHOICES = [
        ('others', 'Others'),
        ('Headq', 'ICMR, Headquarter, New Delhi'),
        ('nicpr', 'NICPR, Noida, Uttar Pradesh'),
        ('nimr', 'NIMR, New Delhi'),
        ('niv', 'NIV, Pune'),
        ('nivmu', 'NIVMU, Mumbai'),
        ('nirrch', 'NIRRCH, Mumbai'),
        ('nie', 'NIE, Chennai'),
    ]
    Name_of_Institutes = models.CharField(max_length=10, choices=STATUS_CHOICES, default='others')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.subject[:20]}'


