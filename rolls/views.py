from django.shortcuts import render
from .models import Roll

# Create your views here.
def rolls(request):
    rolls = Roll.objects.all()
    return render(request, 'rolls/sushi_rolls.html', {'rolls' : rolls})

def contattaci(request):
    return render(request, 'rolls/contattaci.html')