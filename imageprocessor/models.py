from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Image(models.Model):
    profile_pic = models.ImageField(
        upload_to="profile pic"
    )

    profile_pic_thumbnail = ImageSpecField(
        source='profile_pic',
        processors=[ResizeToFill(700, 150)],
        format="JPEG",
        options={
            'quality': 60
        }
    )

    background_pic = models.ImageField(
        upload_to="background pic"
    )

    feature_pic = models.ImageField(
        upload_to="feature pics"
    )

    def get_absolute_url(self):
        return reverse("imageprocessor:update", args=[self.id])

    @property
    def profileURL(self):
        try:
            url = self.profile_pic_thumbnail.url
        except ValueError:
            url = ''
        return url

    @property
    def backgroundURL(self):
        try:
            url_back = self.background_pic.url
        except ValueError:
            url_back = ''
        return url_back

    @property
    def featureURL(self):
        try:
            url_feature = self.feature_pic.url
        except ValueError:
            url_feature = ''
        return url_feature
