from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Bike(models.Model):
    name = models.CharField(max_length=255)
    rider = models.ForeignKey(Rider, related_name='bikes')

    def __unicode__(self):
        return "{} - {}".format(self.rider, self.name)
