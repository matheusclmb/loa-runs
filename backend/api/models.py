from django.db import models

# Create your models here.


class AbyssRaids(models.Model):
    class Meta:
        verbose_name_plural = "Abyss Raids"

    TYPE_CHOICE = (("Abyss Raid", "Abyss Raid"),)

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to="abyssraids/", blank=True, null=True)
    type = models.CharField(max_length=200, choices=TYPE_CHOICE)
    comp = models.IntegerField(default=0)
    gates = models.IntegerField(default=0)
    minimum_level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.type} - {self.minimum_level}"

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""


class LegionRaids(models.Model):
    class Meta:
        verbose_name_plural = "Legion Raids"

    TYPE_CHOICE = (("Legion Raid", "Legion Raid"),)

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to="legionraids/", blank=True, null=True)
    type = models.CharField(max_length=200, choices=TYPE_CHOICE)
    comp = models.IntegerField(default=0)
    gates = models.IntegerField(default=0)
    minimum_level = models.IntegerField(default=0)
    minimum_level2 = models.IntegerField(default=0)
    minimum_level3 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.type} - {self.minimum_level}/{self.minimum_level2}/{self.minimum_level3}"

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""
