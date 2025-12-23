from django.contrib import admin
from django.utils.html import format_html
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image_preview',
        'name',
        'price',
        'type',
        'doors',
        'passengers',
        'transmission',
        'fuel',
        'year',
        'available',
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="60" style="object-fit: cover;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Image"
