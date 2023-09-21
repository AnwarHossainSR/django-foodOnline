from django.shortcuts import render
from vendor.models import Vendor

# Create your views here.

def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    vendor_count = vendors.count()
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }
    return render(request, 'marketplace/listings.html', context)

def vendor_detail(request, vendor_slug):
    pass

def add_to_cart(request, vendor_slug):
    pass

def decrease_cart(request, vendor_slug):
    pass

def delete_cart(request, vendor_slug):
    pass
