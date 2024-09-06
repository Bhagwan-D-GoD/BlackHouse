from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


# Candlestick data
@api_view(['GET'])
def candlestick_data(request):
    data = [
        {"time": "2023-09-01", "open": 120.50, "high": 125.00, "low": 118.30, "close": 122.00},
        {"time": "2023-09-02", "open": 122.00, "high": 124.50, "low": 119.50, "close": 121.75},
        {"time": "2023-09-03", "open": 121.75, "high": 123.50, "low": 117.00, "close": 118.75},
        {"time": "2023-09-04", "open": 118.75, "high": 121.00, "low": 116.00, "close": 119.50},
        {"time": "2023-09-05", "open": 119.50, "high": 122.50, "low": 118.00, "close": 120.50},
    ]
    return Response(data)

# Line chart data
@api_view(['GET'])
def line_chart_data(request):
    data = {
  'labels': ['January', 'February', 'March', 'April', 'May', 'June'],
  'datasets': [
    {
      'label': 'Dataset 1',
      'data': [65, 59, 80, 81, 56, 55],
      'fill': False, 
      'borderColor': 'rgba(75, 192, 192, 1)',
      'tension': 0.1, 
    },
    {
      'label': 'Dataset 2',
      'data': [28, 48, 40, 19, 86, 27],
      'fill': False,
      'borderColor': 'rgba(153, 102, 255, 1)',
      'tension': 0.1,
    },
  ],
}
    return Response(data)

# Bar chart data
@api_view(['GET'])
def bar_chart_data(request):
    data = {
        "labels": ["Product A", "Product B", "Product C"],
        "datasets": [
            {
                "label": "Sales",
                "data": [100, 150, 200],
                "backgroundColor": 'rgba(75,192,192,0.2)',
                "borderColor": 'rgba(75,192,192,1)',
                "borderWidth": 1
            }
        ]
    }
    return Response(data)

# Pie chart data
@api_view(['GET'])
def pie_chart_data(request):
    data = {
        "labels": ["Red", "Blue", "Yellow"],  # X-axis labels
        "datasets": [
            {
                "label": "My Dataset",  # Dataset label
                "data": [300, 50, 100],  # Data points
                "backgroundColor": [
                    'rgba(255, 99, 132, 0.2)', 
                    'rgba(54, 162, 235, 0.2)', 
                    'rgba(255, 206, 86, 0.2)'
                ],  # Background color for each data point
                "borderColor": [
                    'rgba(255, 99, 132, 1)', 
                    'rgba(54, 162, 235, 1)', 
                    'rgba(255, 206, 86, 1)'
                ],  # Border color for each data point
                "borderWidth": 1  # Border width
            }
        ]
    }
    return Response(data)
