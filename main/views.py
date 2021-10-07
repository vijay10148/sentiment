from pickle import GET
from django.http import response
from django.shortcuts import render
from .apps import MainConfig
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.
class call_model(APIView):
    def get(self,request):
       
            text=request.GET.get('text')
            

            vector=MainConfig.vectorizer.transform([text])
            prediction=MainConfig.model.predict(vector)[0]
            context={'showdata':prediction}
#             return render(request,'home.html',context)
            return JsonResponse(context)

# def start(request):
#     if request.method=='GET':

#         data_text=request.POST.get('user')
        
#         vector=MainConfig.vectorizer.transform([data_text])
#         prediction=MainConfig.model.predict(vector)[0]
#         context={'showdata':prediction}
#     else:
#         pass
#     return render(request,'home.html',context)