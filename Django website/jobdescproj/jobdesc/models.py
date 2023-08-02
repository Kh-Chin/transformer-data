from django.db import models
# from 


model = None

# Create your models here.
class JobRequest(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=150)
    about_us = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    keywords = models.CharField(max_length=300)
    job_desc = models.CharField(max_length=7000)

    def predict(self):
        # prompt = ""
        # output = model.generate(prompt)
        # self.job_desc = output.decode()
        self.job_desc = "Predicted"