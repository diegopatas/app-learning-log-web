from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """Return a string representation of the model."""
            return  f"{self.text[:50]}..."

    # _explanation
    # We create an instance of ForeingKey (a way connect a topic to an entry); it has a cascading delete property
    # We create an instance of textfield
    # date_added allows us to present entries in order of creation.
    # Meta is a nest class that manages extra information, in this case, a plural.
    # Meta returns content with max 50 char.