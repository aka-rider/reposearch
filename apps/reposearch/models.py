from django.db import models


class RepoSearch(models.Model):
    """
    The response model of the search endpoint
    """
    id = models.TextField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    web_url = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
