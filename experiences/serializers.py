from rest_framework import serializers

from medias.serializers import PhotoSerializer, VideoSerializer
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer

from .models import Perk, Experience


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceListSerializer(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    photos = PhotoSerializer(read_only=True, many=True)
    videos = VideoSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = (
            "id",
            "host",
            "country",
            "city",
            "name",
            "description",
            "photos",
            "videos",
        )


class ExperienceDetailSerializer(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    perks = PerkSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    photos = PhotoSerializer(read_only=True, many=True)
    videos = VideoSerializer(read_only=True, many=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = "__all__"

    def get_is_owner(self, experience):
        request = self.context["request"]
        return experience.host == request.user
