from .apps import PokemonConfig
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

class call_model(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            model = PokemonConfig.trained_model
            for key, value in data.items():
                data[key] = [value]
            data = pd.DataFrame(data)
            prediction = model.predict(data)
            result = {'Total Power': prediction[0]}
            return Response(result, status = status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)