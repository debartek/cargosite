from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    house_number = models.IntegerField()
    apt_number = models.IntegerField(null=True)
    post_code = models.IntegerField()
    contact_person = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.street + ', ' + self.house_number.__str__() + ', ' + self.apt_number.__str__() + ', ' +  self.post_code.__str__() + ', ' + self.contact_person + ', ' + self.email + ', '+ self.phone.__str__()

class Shipper(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Consignee(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ', ' + self.address.__str__()

class Package(models.Model):
    pack_types = (
            ('EUR', 'Euro Pallet'),
            ('BOX', 'Box'),
            ('BEL', 'Bela'),
            ('BAG', 'Big Bag'),
            ('CHP', 'Chep Pallet'),
            ('PAL', 'Other Pallet')
                )
    pack_type =   models.CharField(max_length=3, choices = pack_types)  
    description = models.CharField(max_length=100)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.pack_type+ ', '+ self.length.__str__() + ', ' + self.width.__str__() + ', ' + self.height.__str__()

class Order(models.Model):
    collect_address = models.ForeignKey(Shipper,on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Consignee,on_delete=models.CASCADE)
    cargo = models.ForeignKey(Package,on_delete=models.CASCADE)
    collect_date = models.DateField()
    delivery_date = models.DateField()
    remarks = models.CharField(max_length=400)
    customer_reference = models.CharField(max_length=10)
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return  "Collect Address: "+ self.collect_address.__str__()+"\n"+ "Delivery Address:"+ self.delivery_address.__str__() + "\n" + "Cargo : " + self.cargo.__str__() + "\n" + "Collect Date: "+ self.collect_date.__str__() +"\n" + "Delivery Date: " + self.delivery_date.__str__()
