from django import forms

from .models import Order, Consignee, Shipper, Address



class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street','house_number', 'apt_number', 'post_code', 'contact_person', 'email', 'phone']


class ShipperForm(forms.ModelForm):
    #address = AddressForm()
    class Meta:
        model = Shipper
        fields = ['name','address']
        field_classes = {
            'address' : AddressForm(),
        }


class OrderForm(forms.ModelForm):
    #collect_address = ShipperForm()
    class Meta:
        model = Order
        fields = ['collect_address', 'delivery_address', 'cargo', 'collect_date', 'delivery_date', 'remarks', 'customer_reference']
        field_classes = {
            'collect_address' : ShipperForm(),
        }