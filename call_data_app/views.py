from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utility import parse_customer_data, parse_call_data, match_calls_with_customers, get_msdin

class CallDataAPIView(APIView):
    def get(self, request):
        params = request.GET
        print(params)
        call_data = parse_call_data()
        #params = {'name':'Shiney'}
        # params = {'msdin': '+15551234567'}
        customer_data = parse_customer_data()
        
        msdin = get_msdin(customer_data,params)
        print(msdin)
        matched_calls = match_calls_with_customers(call_data, customer_data, msdin)
        return Response(matched_calls)
