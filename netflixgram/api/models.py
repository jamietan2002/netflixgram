from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        #user_profile.follows.add(instance.profile)
        #user_profile.save()

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(
        User, related_name="reviews", on_delete=models.DO_NOTHING
    )
    movie = models.CharField(max_length=100)
    my_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    my_review = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.movie} "
            f"{self.my_rating} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.my_review[:30]}..."
        )



