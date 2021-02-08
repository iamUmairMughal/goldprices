from django.http import JsonResponse
from rest_framework.decorators import api_view
from .gold_prices import find_price
import json
from rest_framework.generics import ListCreateAPIView
class Img_to_Test(ListCreateAPIView):

    @api_view(['POST'])
    def post(country_data):
        data = json.loads(country_data.body)
        c_name = str(data.get('country'))
        s_type = str(data.get('scale'))
        price = find_price(c_name, s_type)
        if  price == "ERROR":
            return JsonResponse('Error', safe=False)
        elif price == 'NULL':
            return JsonResponse('NULL', safe=False)
        else:
            return JsonResponse({'price' : str(price)}, safe=False)