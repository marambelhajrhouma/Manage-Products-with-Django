from django.shortcuts import render,redirect
from django.db.models import Max
from product.models import Product
from product.forms import ProductForm

# Create your views here.

# Create new product + redirecte the user to show
def prod(request):  
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProductForm() #vide

    return render(request, 'index.html', {'form': form})

#récupère tous les produits de la BDD Product + par render nous retourne ç la page show
def show(request):
    products = Product.objects.all() #récupère tous les donnés de BDD NOM TAB pRODUCT
    product_count = products.count()  # Count the number of products
    return render(request, "show.html", {'products': products, 'product_count': product_count})

# concerne l'affichage du formulaire d'édition
#en utilisant render : renvoie la page d'édition avec les détails de ce produit
def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'edit.html', {'product': product})

#concerne le traitement de la soumission du formulaire et la mise à jour des données
def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    
    if form.is_valid():
        form.save()
        return redirect("/show")
    
    return render(request, 'edit.html', {'product': product})

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return redirect("/show")

def search_product(request):
    query = request.GET.get('q')
    products = Product.objects.all()

    if query:
        products = Product.objects.filter(pname__icontains=query)

    return render(request, "show.html", {'products': products, 'query': query})

def search_by_price(request):
    query = request.GET.get('price')
    products = Product.objects.filter(price__lte=query) if query else Product.objects.all()
    # Product.objects.filter(price__lte=query): renvoie tous les produits dont le prix est inférieur ou égal à la valeur 
    return render(request, "show.html", {'products': products, 'query': query})
