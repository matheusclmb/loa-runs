from rest_framework import serializers
from .models import *


class AbyssRaidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbyssRaids
        fields = (
            "name",
            "type",
            "comp",
            "gates",
            "minimum_level",
            "get_image",
            "slug",
            "image",
        )

class LegionRaidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegionRaids
        fields = (
            "name",
            "type",
            "comp",
            "gates",
            "minimum_level",
            "minimum_level2",
            "minimum_level3",
            "get_image",
            "slug",
            "image",
        )

class RunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runs
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    date =  serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = Blog
        fields = '__all__'