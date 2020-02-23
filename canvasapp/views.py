from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context, Template
from django.core.urlresolvers import reverse
from .models import Canvas
from rest_framework.views import APIView
from rest_framework.response import Response
from canvasapp.mongo import *
# from django.views.decorators.csrf import csrf_exempt



class canvas(APIView):
    def post(self, request):
        x = request.POST.get('xcoord')
        y = request.POST.get('ycoord')
        color = request.POST.get('color')
        print("in canvas post")
        drawing = createdrawing(x,y,color)
        return Response()

def homepage(request):
    drawing = getdrawing()
    # print(list(drawing))
    context = {"drawing" : drawing}
    return render(request, 'index.html', context)

def draw(request):
    drawing = getdrawing()
    # print(list(drawing))
    context = {"drawing" : drawing}
    return render(request, 'draw.html', context)

class update(APIView):
    def get(self,request):
        update = getdrawing()
        for doc in update:
            doc.pop("_id")
        # update = list(update)
        print(update)
        return JsonResponse({"update" : update})

# def drawRedirect(request):
#     return HttpResponseRedirect(reverse("draw"))



