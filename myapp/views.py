from django.shortcuts import render
from django.http import HttpResponse
import joblib

def index(request):
    return render(request, "myapp/index.html", {})

def classify_view(request):
    if request.method == 'GET':
        # Get the input data from the request
        preg = float(request.GET.get('preg', 0))
        gluc = float(request.GET.get('gluc', 0))
        blood = float(request.GET.get('blood', 0))
        skin = float(request.GET.get('skin', 0))
        ins = float(request.GET.get('ins', 0))
        bmi = float(request.GET.get('bmi', 0))
        dbf = float(request.GET.get('dbf', 0))
        age = float(request.GET.get('age', 0))

        # Load the saved machine learning model
        model_filename = "C:/Users/djaba/mydjangosite/logistic_regression_model.pkl"
        loaded_model = joblib.load(model_filename)

        # Define sample input data
        sample_input = [[preg, gluc, blood, skin, ins, bmi, dbf, age]]

        # Make predictions using the loaded model
        predicted = loaded_model.predict(sample_input)
        predicted_category = "You are Diabetic!" if predicted[0] == 1 else "You are Non-Diabetic!"

        # Render the result directly in the index.html template
        return render(request, 'myapp/index.html', {'Category': predicted_category})

    # If the request method is not GET, you can handle it accordingly
    return HttpResponse("Invalid request method")
