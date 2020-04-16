from django.shortcuts import render

from plants.models import Plant

# Create your views here.
def plant_list(request):
    context = {
        "all_plants": Plant.objects.all()
    }
    return render(request, 'plant_list.html', context)
