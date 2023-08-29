from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from station.models import Bus
from station.serializers import BusSerializer


@api_view(["GET", "POST"])
def bus_list(request):
    if request.method == "GET":
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def bus_detail(request, pk):
    try:
        bus = Bus.objects.get(pk=pk)
    except Bus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BusSerializer(bus)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BusSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

