from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel
from .validators import validate_video_file, validate_image_file


class User(AbstractUser):
    email = models.EmailField(max_length=100)
    pass


class Visibility:
    PUBLIC = 'PUBLIC'
    FRIENDS_ONLY = 'FRIENDS ONLY'
    PRIVATE = 'PRIVATE'
    VIEW_GROUP = (
        (PUBLIC, "PUBLIC"),
        (PRIVATE, "FRIENDS ONLY"),
        (PRIVATE, "PRIVATE"),
    )


class Profile(TimeStampedModel):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    profile_image = models.ImageField(
        upload_to='./images/profile', blank=True, null=True, validators=[validate_image_file])

    class Meta:
        permissions = [
            ('can_view_content', 'can view content'),
            ('can_edit_content', 'can edit content'),
        ]
    def __str__(self):
        return f"{self.name}"

class Video(TimeStampedModel):
    visibility = Visibility()
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='user_video')
    caption = models.CharField(max_length=50)
    video_description = models.CharField(max_length=50)
    video_file = models.FileField(
        upload_to='./videos', validators=[validate_video_file])

    VIEW_GROUP_CHOICE = models.CharField(
        choices=visibility.VIEW_GROUP, default="None", max_length=500, null=True, blank=True
    )
    def __str__(self):
        return f"{self.user.name} {self.caption}"

class Image(TimeStampedModel):
    visibility = Visibility()
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='user_image')
    user_images = models.ImageField(
        upload_to='./images/pictures', blank=True, null=True, validators=[validate_image_file])
    image_title = models.CharField(max_length=50, null=True, blank=True)
    image_description = models.CharField(max_length=50, null=True, blank=True)
    VIEW_GROUP_CHOICE = models.CharField(
        choices=visibility.VIEW_GROUP, default="None", max_length=500, null=True, blank=True
    )
    def __str__(self):
        return f"{self.user.name} {self.image_title}"

class Post(TimeStampedModel):
    visibility = Visibility()
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='user_post')
    post_title = models.CharField(max_length=50, null=True, blank=True)
    post_description = models.CharField(max_length=250, null=True, blank=True)
    VIEW_GROUP_CHOICE = models.CharField(
        choices=visibility.VIEW_GROUP, default="None", max_length=500, null=True, blank=True
    )
    def __str__(self):
        return f"{self.user.name} {self.post_title}"