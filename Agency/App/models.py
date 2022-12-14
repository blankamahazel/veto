from django.db import models

# 1) PREVENT DUPLICACTED EMAILS
class Registered_email(models.Model):
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.email

# 2 SUPPORT 
class Support(models.Model):

    PERSON = {
        ('Employee', 'Employee'),
        ('Candidate', 'Candidate'),
    }

    OPTION = {
        ('I lost my account', 'I lost my account'),
        ('My password does not work', 'My password does not work'),
        ('Update resume', 'Update resume'),
        ('Others', 'Others'),
    }

    SITUATION = {
        ('Done', 'Done'),
        ('Pending', 'Pending'),
    }

    terms = models.BooleanField("took responsibility", default=False)
    message = models.TextField()
    person = models.CharField(max_length=50, choices=PERSON)
    option = models.CharField(max_length=50, choices=OPTION)
    email = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')

    def __str__(self):
        return self.person