from .serializers import DessertSerializer
from .models import Dessert
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def getDesserts(request):
    all_desserts = Dessert.objects.all()
    # lekérjük az összes desszertet
    serialized = DessertSerializer(all_desserts, many=True)
    # serializálunk
    return Response(serialized.data)
    # visszaadjuk a serializált adatokat