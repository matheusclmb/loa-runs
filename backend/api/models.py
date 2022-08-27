from tabnanny import verbose
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


class Runs(models.Model):
    class Meta:
        verbose_name_plural = "Runs"

    TYPE_CHOICE = (("Abyss Raid", "Abyss Raid"), ("Legion Raid", "Legion Raid"))

    RAID_NAMES = (
        ("Argos", "Argos"),
        ("Valtan", "Valtan"),
        ("Vykas", "Vykas"),
        ("Kakul-Saydon", "Kakul-Saydon"),
    )

    DIFFICULTIES = (
        ("Normal", "Normal"),
        ("Hard", "Hard"),
        ("Inferno", "Inferno"),
    )

    youtube = models.URLField(blank=True, null=True)
    screenshot = models.ImageField(upload_to="runs/", blank=True, null=True)
    raid_type = models.CharField(max_length=200, choices=TYPE_CHOICE)
    raid_name = models.CharField(max_length=200, choices=RAID_NAMES)
    difficulty = models.CharField(max_length=200, choices=DIFFICULTIES)
    time = models.CharField(max_length=10)
    deathless = models.BooleanField(default=False)
    discord = models.CharField(max_length=200)

    playerOne = models.CharField(max_length=200)
    playerTwo = models.CharField(max_length=200)
    playerThree = models.CharField(max_length=200, blank=True, null=True)
    playerFour = models.CharField(max_length=200, blank=True, null=True)
    playerFive = models.CharField(max_length=200, blank=True, null=True)
    playerSix = models.CharField(max_length=200, blank=True, null=True)
    playerSeven = models.CharField(max_length=200, blank=True, null=True)
    playerEight = models.CharField(max_length=200, blank=True, null=True)

    playerOneLVL = models.IntegerField(default=0)
    playerTwoLVL = models.IntegerField(default=0)
    playerThreeLVL = models.IntegerField(default=0, blank=True, null=True)
    playerFourLVL = models.IntegerField(default=0, blank=True, null=True)
    playerFiveLVL = models.IntegerField(default=0, blank=True, null=True)
    playerSixLVL = models.IntegerField(default=0, blank=True, null=True)
    playerSevenLVL = models.IntegerField(default=0, blank=True, null=True)
    playerEightLVL = models.IntegerField(default=0, blank=True, null=True)
    averageIlvl = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        players = [
            self.playerOneLVL,
            self.playerTwoLVL,
            self.playerThreeLVL,
            self.playerFourLVL,
            self.playerFiveLVL,
            self.playerSixLVL,
            self.playerSevenLVL,
            self.playerEightLVL,
        ]

        valid_players = []

        for i in players:
            if i > 0:
                valid_players.append(i)

        self.averageIlvl = sum(valid_players) / len(valid_players)

        super(Runs, self).save(*args, **kwargs)

    def __str__(self):
        return f"N: {self.raid_name} - D: {self.difficulty} - T: {self.time} - {self.discord}"
