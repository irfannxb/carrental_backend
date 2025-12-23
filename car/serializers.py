from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    # Extra read-only field to expose absolute URL, while keeping the real image
    image_url = serializers.SerializerMethodField(read_only=True)
    # Make user field read-only so it can't be set manually (will be set in view)
    # user = serializers.PrimaryKeyRelatedField(rea)

    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'image',
            'price',
            'type',
            'doors',
            'passengers',
            'transmission',
            'fuel',
            'year',
            'available',
            'user',
            'image_url',
        ]

    def get_image_url(self, obj):
        request = self.context.get('request')  # Get the request context
        if request and obj.image:
            # Build the absolute URL for the image
            return request.build_absolute_uri(obj.image.url)
        return None
