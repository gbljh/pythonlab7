from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, SensorCategory
from rest_framework.views import APIView
from rest_framework.views import Response
from .serializer import SensorSerializer
from django.views.generic import CreateView
from django.views.generic import View
from django.utils import timezone
from .render import Render


def index(request):
    return render(request, "index.html")

def sensor(request, id):
    sensor = Sensor.objects.filter(id=id).values()
    category = SensorCategory.objects.filter(id=list(sensor)[0]['category_id']).values()
    return render(request, "sensor.html", context={"sensor": list(sensor)[0], "category": list(category)[0]})

def sensors(request):
    sensors = Sensor.objects.all()
    return render(request, "sensors.html", context={"sensors": list(sensors)})


def success(request, data):
    return render(request, "success.html", context={"data": data})



###zapolnenie form###
class SensorCategoryCreateView(CreateView):
    template_name = 'create/sensor_category_create.html'
    success_url="/success/sensor_category/"
    model = SensorCategory
    fields = ('name',)

class SensorCreateView(CreateView):
    template_name = 'create/sensor_create.html'
    success_url="/success/sensor/"
    model = Sensor
    fields = ('lon', 'lat', 'create_date', 'name', 'model', 'category',)

######################






###JSON EXPORT MODELS###
class StockList(APIView):

    def get(self, request):
        stocks = Sensor.objects.all()
        serializer = SensorSerializer(stocks, many=True) 
        return Response(serializer.data)
           

    def post(self):
        pass
#############################



###pdf_file##################
class Pdf(View):
    def get(self, request):
        sensorpdfs = Sensor.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sensorpdfs': sensorpdfs,
            'request': request
        }
        return Render.render('pdf.html', params)

############################