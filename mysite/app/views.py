from django.http import HttpResponse



def index(request):
    return HttpResponse(" <h3> sumar/x/y , restar/x/y, multiplicar/x/y </h3>")
def sum(request, num1, num2):
    sum = num1 + num2
    return HttpResponse("<h3>La suma de {} + {}  = {}</h3>".format(num1,num2,sum))
def rest(request, num1, num2):
    rest = num1 - num2
    return HttpResponse("<h3>La resta de {} - {}  = {}</h3>".format(num1,num2,rest))
def multiplicacion(request, num1, num2):
    multiplicacion = num1 * num2
    return HttpResponse("<h3>La multiplicacion de {} x {}  = {}</h3>".format(num1,num2,multiplicacion))