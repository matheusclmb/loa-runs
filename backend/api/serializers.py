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
