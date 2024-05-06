from django.shortcuts import render
def max_of_five(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        num3 = int(request.POST['num3'])
        num4 = int(request.POST['num4'])
        num5 = int(request.POST['num5'])

        max_number = num1

        if num2 > max_number:
            max_number = num2
        if num3 > max_number:
            max_number = num3
        if num4 > max_number:
            max_number = num4
        if num5 > max_number:
            max_number = num5

    return render(request, 'max_number.html', {'max_number': max_number})
