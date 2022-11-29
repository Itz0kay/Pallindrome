from django.db import models

# Create your models here.

class Pallindrome(models.Model):
    name = models.CharField(max_length=20)
    p_or_not = models.CharField(max_length=20,blank=True)

    # def __init__(self) -> None:
    #     return self.name

    def clean(self):
        if self.name == self.name[::-1]:
            self.p_or_not = "Yes"
        else:
            self.p_or_not = "No"
