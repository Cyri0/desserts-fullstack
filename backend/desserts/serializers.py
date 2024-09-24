from rest_framework.serializers import ModelSerializer
from .models import Dessert, DessertCategory

class DessertSerializer(ModelSerializer):
    class Meta:
        model = Dessert
        fields = "__all__"
        depth = 1

class DessertCategorySerializer(ModelSerializer):
    class Meta:
        model = DessertCategory
        fields = "__all__"
