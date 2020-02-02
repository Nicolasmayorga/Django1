"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

<<<<<<< HEAD
=======
    
>>>>>>> a79312ad0be2a2ebefbbb00761b06bf21f937bf5
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
<<<<<<< HEAD
        return '{} by @{}'.format(self.title, self.user.username)
=======
        return '{} by @{}'.format(self.title, self.user.username)
>>>>>>> a79312ad0be2a2ebefbbb00761b06bf21f937bf5
