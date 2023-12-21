from django.db import models


class NewsChannels(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class NewsSection(models.Model):
    name = models.CharField(max_length=30)
    newsChannel = models.ForeignKey(NewsChannels, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.name


class NewsHeaders(models.Model):
    name = models.CharField(max_length=30)
    newsSection = models.ForeignKey(NewsSection, on_delete=models.CASCADE, related_name='headers')
    date = models.DateField()
    description = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    post = models.CharField(max_length=500)
    country = models.CharField(max_length=30)
    extraNews = models.BooleanField()

    def __str__(self):
        return self.name + ' ' + self.author