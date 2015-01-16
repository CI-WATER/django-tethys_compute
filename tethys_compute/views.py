from django.shortcuts import render
from django.http import HttpResponse
from starcluster_api import StarCluster

from tethys_compute.models import TethysJob

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the compute index.")

def create_cluster(request):
    sc = StarCluster()



