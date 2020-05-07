from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser

from .models import Sensor
from .serializers import SensorDetailSerializer, SensorListSerializer


class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def sensor(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # Fetches the first result of Sensor with name=data['name']
        sensor = Sensor.objects.filter(name=data['name']).first()

        if sensor:
            serializer = SensorDetailSerializer(instance=sensor, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)

        else:
            serializer = SensorDetailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)


def chart(request):
    # Fetches all sensor objects
    sensor = Sensor.objects.all()
    # GET sensor data
    if sensor:
        for s in sensor:
            name = s.name
            kind = s.kind
            values = s.values
            times = [times for times in range(1, len(values))]


        context={
            'sensor': sensor,
            'name':name,
            'kind':kind,
            'values': values,
            'times':times
        }
        return render(request, 'application/chart.html', context)
    return render(request, 'application/chart.html')
