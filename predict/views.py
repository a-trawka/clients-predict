from django.shortcuts import render

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from sklearn.linear_model import LinearRegression

import os


def predict(request):
    data = pd.read_csv('clients_data.csv')
    df = pd.DataFrame(data)
    x = df[['days_since_start']]
    y = df['clients']
    prediction = LinearRegression()
    prediction.fit(x, y)
    predicted = prediction.predict(100)
    p = os.path.dirname(__file__)
    if not os.path.isfile(f'{p}/static/images/clients_point_plot.png'):
        plt.plot(x, y, 'b.')
        blue_line = mlines.Line2D([], [], color='blue', label='CSV DATA')
        red_dot = mlines.Line2D([], [], color='red', marker='o', label='prediction', linewidth=0)
        plt.legend(handles=[blue_line, red_dot])
        plt.plot(100, float(predicted), 'ro')
        plt.xlabel('Days since start')
        plt.ylabel('Number of clients')
        plt.savefig(f'{p}/static/predict/images/clients_point_plot.png')
        plt.clf()
    if not os.path.isfile(f'{p}/static/images/clients_line_plot.png'):
        plt.plot(x, y, 'b')
        blue_line = mlines.Line2D([], [], color='blue', label='CSV DATA')
        red_dot = mlines.Line2D([], [], color='red', marker='o', label='prediction', linewidth=0)
        plt.legend(handles=[blue_line, red_dot])
        plt.plot(100, float(predicted), 'ro')
        plt.xlabel('Days since start')
        plt.ylabel('Number of clients')
        plt.savefig(f'{p}/static/predict/images/clients_line_plot.png')
        plt.clf()
    return render(request, 'predict/predict.html', {'predict_clients': int(predicted)})
