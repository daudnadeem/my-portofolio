from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        if(len(self.body) > 100):
            summary_ = self.body[:100] + str("...")
        else:
            return self.body
        return summary_
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')