from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('sum/<int:num1>/<int:num2>', views.sum, name='sum'),

    path('rest/<int:num1>/<int:num2>', views.rest, name='rest'),
    
    path('multiplicacion/<int:num1>/<int:num2>', views.multiplicacion, name='multiplicacion'),
]

