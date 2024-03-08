from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


# Create your views here.
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


# class SensorsView(APIView):
#     def get(self, request):
#         sensor = Sensor.objects.all()
#         ser = SensorDetailSerializer(sensor, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         post_new = Sensor.objects.create(
#             name=request.data['name'],
#             description=request.data['description'],
#         )
#         return Response({'status': 'OK', 'added': model_to_dict(post_new)})
#
#     def patch(self, request):
#         patch_new = Sensor.objects.get(request.data['id'])
#         serializer = SensorDetailSerializer(patch_new, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'OK', 'added': model_to_dict(patch_new)})
#         return Response({'status': 'ERROR'})
#
#
# class SensorView(RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#
#
# class MeasurementView(APIView):
#     def get(self, request):
#         sensor = Measurement.objects.all()
#         ser = MeasurementSerializer(sensor, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         post_new = Measurement.objects.create(
#             temperature=request.data['temperature'],
#         )
#         return Response({'status': 'OK', 'added': model_to_dict(post_new)})

class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class ListSensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveSensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
