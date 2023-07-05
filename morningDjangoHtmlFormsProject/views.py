from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def add_product(request):

    if request.method == "POST":
        prod_name = request.POST.get("p-name")
        prod_quantity = request.POST.get("q-tty")
        prod_size = request.POST.get("p-size")
        prod_price = request.POST.get("p-name")
        context = {
                   "prod_name": prod_name,
                   "prod_quantity": prod_quantity,
                   "prod_size": prod_size,
                   "prod_price": prod_price,
                   }
        return render(request,'add-product.html', context)
    return render(request, 'add-product.html',)
