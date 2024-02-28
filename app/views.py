from django.http import HttpRequest , HttpResponse ,JsonResponse
import json
from.models import smartfan 

smartfon=smartfan


# Create your views here.

def add(reqeust : HttpRequest):
    if reqeust.method=='POST':
        d=reqeust.body.decode('UTF-8')
        data=json.loads(d)
        price  =data['price'],
        img_url=data['img_url'],
        color  =data['color']
        ram    =data['ram'],
        memory =data['memory'],
        name   =data['name'],
        model  =data['model'],

        produk=smartfon.objects.create(
          price  =price,
          img_url=img_url,
          cilor  =color,
          ram    =ram,
          memory =memory,
          name   =name,
          model  =model  
        )
        produk.save()

        return JsonResponse({'salom': 'salom'})
    



     
    
def get(reqeust : HttpRequest , pk) -> JsonResponse:
    if reqeust.method=='GET':
    
        data=smartfon.objects.get(id=pk)
        a={
        "price"  :data.price,
        "img_url":data.img_url,
        "color"  :data.cilor,
        "ram "   :data.ram,
        "memory" :data.memory,
        "name"   :data.name,
        "model"  :data.model,

        }



        return  JsonResponse({pk : a})

        

def get_all(reqeust : HttpRequest) -> JsonResponse:
    data=smartfon.objects.all()
    
    a=[]
    for i in data:
    
        a.append(i.to_dict())
    # print(a , "salom")

    return JsonResponse({"smartfon " : a})




def delete(reqeust : HttpRequest , pk):
    a=smartfon.objects.filter(id=pk).delete()

    return JsonResponse({"smartfon_delete" : "oK"})





def updete(reqeust : HttpRequest):

    pass





