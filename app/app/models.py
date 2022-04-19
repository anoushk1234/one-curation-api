from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=200)
    gallery = ArrayField(
        models.URLField(max_length=200),
    )
    logo = models.URLField(max_length=200)

    def __str__(self):
        return (
            self.name,
            self.description,
            self.created_at,
            self.updated_at,
            self.website,
            self.gallery,
            self.logo,
        )


class ProjectPosts(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField(max_length=200)

    def __str__(self):
        return (
            self.project,
            self.title,
            self.description,
            self.created_at,
            self.updated_at,
            self.image,
        )
