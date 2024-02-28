from django.db import models

# Create your models here.

class smartfan(models.Model):

        price  =models.CharField(max_length=255)
        img_url=models.CharField(max_length=255)
        cilor  =models.CharField(max_length=255)
        ram    =models.CharField(max_length=255)
        memory =models.CharField(max_length=255)
        name   =models.CharField(max_length=255)
        model  =models.CharField(max_length=255)

        def __str__(self):
            return self.name 


        def to_dict(self):
            """
            Convert model to dictionary
            """
            return {
                'id': self.id,
                'price': self.price,
                'url': self.img_url,
                'color': self.cilor,
                'ram': self.ram,
                'memory': self.memory,
                'name': self.name,
                'model': self.model
            }


