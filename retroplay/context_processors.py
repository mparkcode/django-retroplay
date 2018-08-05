from products.models import Brand

def get_brands(request):
    brands = Brand.objects.all()
    return{"all_brands":brands}