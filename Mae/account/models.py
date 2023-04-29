from django.db import models
from django.conf import settings


# class ClientProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ClientInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class CaseTypes(models.TextChoices):
        ALL = "0", "ALL"
        CRIMINAL = "1", "CRIMINAL"
        CIVIL = "2", "CIVIL"

    case_type = models.CharField(max_length=1, choices=CaseTypes.choices, default=CaseTypes.ALL)

    residence_state = models.CharField(max_length=2)
    incident_state = models.CharField(max_length=2)

    incident_description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.case_type.lower()} - {self.incident_description.lower()}"

# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     date_of_birth = models.DateField(blank=True, null=True)

#     def __init__(self, *args, **kwargs):
#         super().__init__(args, kwargs)
#         self.photo = models.ImageField(upload_to=f'users/{self.user.username}/')

#     def __str__(self):
#         return f'Profile of {self.user.username}'
