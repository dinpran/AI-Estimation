from django.shortcuts import render, HttpResponse
from .model import CO2EmissionModel

def index(request):
    context = {"variable": "55"}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def emissions(request):
    return render(request, 'emission.html')

def contact(request):
    return render(request, 'contact.html')

def add_inputs(request):
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('1st_input'))
            num2 = float(request.POST.get('2nd_input'))
            result = num1 + num2
        except (ValueError, TypeError):
            result = "Invalid input. Please enter valid numbers."

        return render(request, 'result.html', {'result': result})
    return HttpResponse("Invalid request method.")

def predict_inputs(request):
    if request.method == 'POST':
        try:
            engine_size = float(request.POST.get('1st_input'))
            cylinders = float(request.POST.get('2nd_input'))

            # Predict the CO2 emissions
            model = CO2EmissionModel()
            result = model.predict(engine_size, cylinders)

        except (ValueError, TypeError) as e:
            result = f"Invalid input. Error: {str(e)}"

        return render(request, 'x_result.html', {'result': result})
    return HttpResponse("Invalid request method.")


