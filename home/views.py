from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class Home(APIView):
    def get(self,request):
        # name = request.GET['name']
        # name = request.query_params['name']
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons,many=True)
        return Response(data=ser_data.data)

    # def post(self,request):
    #     name = request.data['name']
    #     return Response({'name':name})