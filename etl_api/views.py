from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data_transform.read_data import items_counter
import pandas as pd

# Create your views here.

df = pd.read_csv('./DataRedesSociales.csv')

class DataResume(APIView):
    def get(self,request):
       response= items_counter(df)
       return Response(response,status=status.HTTP_200_OK)