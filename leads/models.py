from django.db import models
# from django.contrib.auth import get_user_model # function that allows you to use user model provided by Django
# User = get_user_model()

from django.contrib.auth.models import AbstractUser

class User(AbstractUser): # inherit from AbstractUser to get barebones fileds for user
    pass

class Lead(models.Model):
    
    # SOURCE_CHOICES = (
    #     ("YouTube", "YouTube") # (VALUE stored in DB, VALUE that gets displayed)
    #     ("Google", "Google") # (VALUE stored in DB, VALUE that gets displayed)
    #     ("Newsletter", "Newsletter") # (VALUE stored in DB, VALUE that gets displayed)
    # )
    
    first_name = models.CharField(max_length=20) # always provide maximum lenghts
    last_name = models.CharField(max_length=20, default="Jeff")
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) # Create Link to Agent Model/ DB. Could use Agent without "", but then Agent must be definded before Leads. 
                                       # This way with "", Django is told to look for Agent somewhere in the file
                                       # ForeignKeys take the model name and always an on_delete positional argument, tells django what to do if related table row/instance is deleted
    
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100) # Choices don't actually restrict the value that goes into the db 
    
    # profile_picture = models.ImageField(blank=True, null=True) # making pic optional | blank-> for submitting empty string | null -> for having empty db value
    # special_files = models.FileField(blank=True, null=True) # saves reference/link to where file is stored in static

    def __str__(self): # returns the string representation of the model 
        return f"{self.first_name} {self.last_name}" 

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # ForeignKey not best option because we want to have only one user to be associated with one Agent . FK allows many agents for one user

    def __str__(self): # returns the string representation of the model 
        return self.user.email
