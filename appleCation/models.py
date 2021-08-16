from django.db import models
import datetime

'''
define a simple user.
'''


class Cat(models.Model):
    # login
    userName = models.CharField(max_length=20, unique=True)
    userPassword = models.CharField(max_length=20)

    # page access: assigned random string
    accessKey = models.CharField(max_length=200, default="NEWCAT")

    def __str__(self):
        return self.userName


'''
a job application.
'''


class Apple(models.Model):
    # many-to-one Apple:Cat
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, default=1)

    # basic info
    company = models.CharField(max_length=200)
    jobTitle = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    submittedDate = models.DateField(default=datetime.date.today)

    # some optional info
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    statusCheck = models.CharField(null=True, blank=True, max_length=200)

    # online assessment
    OAStatusChoices = (
        ("None", "None"),
        ("Not Started", "Not Started"),
        ("Completed", "Completed"),
    )
    OAstatus = models.CharField(
        max_length=20, choices=OAStatusChoices, default="None")
    OAdue = models.DateTimeField(null=True, blank=True)
    OAlink = models.DateTimeField(null=True, blank=True)

    OAThoughtsChoices = (
        ("meh", "meh"),
        ("hype", "hype"),
        (":(", ":(")
    )
    OAthoughts = models.CharField(
        max_length=5, choices=OAThoughtsChoices, default="meh")

    # status
    pending = models.BooleanField(default=True)
    rejected = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    interviewInvite = models.BooleanField(default=False)
    interviewDate = models.DateField(null=True, blank=True)

    def __str__(self):
        returnstr = self.jobTitle + ", " + self.company
        return returnstr
