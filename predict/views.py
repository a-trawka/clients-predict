from django.http import HttpResponse

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import os


def predict(request):
    data = pd.read_csv('clients_data.csv')
    df = pd.DataFrame(data)
    x = df[['days_since_start']]
    y = df['clients']
    if not os.path.isfile('clients_plot.png'):
        plt.plot(x, y)
        plt.xlabel('Days since start')
        plt.ylabel('Number of clients')
        plt.savefig('clients_plot.png')
    prediction = LinearRegression()
    prediction.fit(x, y)
    return HttpResponse(prediction.predict([3]))
