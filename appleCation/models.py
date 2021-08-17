from django.db import models
import datetime

'''
define a simple user = applicant = AppleCat = Cat
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
a job application = Apple
'''


class Apple(models.Model):
    # many-to-one Apple:Cat
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, default=1)

    # basic info
    company = models.CharField(max_length=200)
    jobTitle = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    submittedDate = models.DateField(default=datetime.date.today)

    # status
    pending = models.BooleanField(default=True)
    rejected = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    # optional info
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        returnstr = self.jobTitle + ", " + self.company
        return returnstr


'''
optional AppleOA
'''


class AppleOA(models.Model):
    # many-to-one with Apple
    apple = models.ForeignKey(Apple, on_delete=models.CASCADE, default=1)

    # online assessment
    OAName = models.CharField(max_length=20, default=" ")
    OADue = models.DateTimeField(null=True, blank=True)
    OALink = models.TextField(null=True, blank=True)

    # status
    OAStatus = models.CharField(max_length=20, default="Not Completed")

    # OA reflection
    OARef = models.CharField(max_length=5, default="None")


'''
optional AppleInterview
'''


class AppleInterview(models.Model):
    # many-to-one with Apple
    apple = models.ForeignKey(Apple, on_delete=models.CASCADE, default=1)

    # interview
    interviewName = models.CharField(max_length=50, default=" ")
    interviewDate = models.DateTimeField(default=datetime.date.today)
    interviewLink = models.TextField(null=True, blank=True)

    # status
    interviewStatus = models.CharField(max_length=20, default="Not Completed")

    # interview reflection
    interviewRef = models.CharField(max_length=5, default="None")
