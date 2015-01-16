from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied

from starcluster.api import StarCluster
from tethys_compute.models import TethysJob, Cluster

# Create your views here.

def index(request):
    clusters = Cluster.objects.all()
    return render(request, 'tethys_compute/cluster_index.html', {'clusters':clusters})


def create_cluster(request):
    name = 'New Cluster'
    size = 2
    if request.POST:
        name = request.POST['name']
        size = int(request.POST['size'])
        cluster = Cluster(name=name, size=size)
        cluster.save()
        try:
            sc = StarCluster()
            #sc.start(name, cluster_size=size)
        except:
            return HttpResponseServerError('There was an error with TethysCluster')
        return redirect(reverse('index'))
    else:
        raise Exception


def delete_cluster(request, pk):
    cluster = get_object_or_404(Cluster, id=pk)
    name = cluster.name
    cluster.delete()
    try:
        sc = StarCluster()
        #sc.terminate(name)
    except:
        HttpResponse('There was an error with TethysCluster')
    return redirect(reverse('index'))
