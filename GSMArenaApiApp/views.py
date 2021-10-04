import requests
from django.shortcuts import render
from django.utils.html import strip_tags
from rest_framework import viewsets

from GSMArenaApiApp.models import Phone
from GSMArenaApiApp.serializers import PhoneSerializer


class PhoneDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    # permission_classes = [IsAuthenticated]
    # authorization_classes = [TokenAuthentication]

    def get_queryset(self):
        phoneModel = self.request.query_params.get('model')
        queryset = Phone.objects.filter(model=phoneModel)
        if queryset.count() > 0:
            return queryset.all()
        else:
            url = "https://m.gsmarena.com/res.php3"
            arg = {"sSearch": phoneModel}
            webscrap = requests.get(url, params=arg)
            name1 = webscrap.text.split('swiper-half-slide">')[1].split("<a href=")[1].split(">")[0]
            newUrl = "https://m.gsmarena.com/" + name1
            phoneScrap = requests.get(newUrl)
            try:
                name = phoneScrap.text.split("<title>")[1].split("- Full phone specifications")[0]
            except:
                name = ""
                pass
            try:
                model = phoneModel
            except:
                model = ""
                pass
            # try:
            #     photo = phoneScrap.text.split('HISTORY_ITEM_IMAGE = "')[1].split('";')[0]
            #     print(photo)
            #     img_data = requests.get(photo).content
            #     print(img_data)
            #     with open('static/phones/' + name1.split(".php")[0] + '.jpg', 'wb') as handler:
            #         handler.write(img_data)
            #     photo = "../../static/phones/" + name1.split(".php")[0] + '.jpg'
            # except:
            #     photo = ""
            #     pass
            # try:
            #     technology = strip_tags(phoneScrap.text.split('data-spec="nettech">')[1].split("</td>")[0])
            # except:
            #     technology = ""
            #     pass
            # try:
            #     band2g = strip_tags(phoneScrap.text.split('data-spec="net2g">')[1].split("</td>")[0])
            # except:
            #     band2g = ""
            #     pass
            # try:
            #     band3g = strip_tags(phoneScrap.text.split('data-spec="net3g">')[1].split("</td>")[0])
            # except:
            #     band3g = ""
            #     pass
            # try:
            #     band4g = strip_tags(phoneScrap.text.split('data-spec="net4g">')[1].split("</td>")[0])
            # except:
            #     band4g = ""
            #     pass
            # try:
            #     speed = strip_tags(phoneScrap.text.split('data-spec="speed">')[1].split("</td>")[0])
            # except:
            #     speed = ""
            #     pass
            # try:
            #     announced = strip_tags(phoneScrap.text.split('data-spec="year">')[1].split("</td>")[0])
            # except:
            #     announced = ""
            #     pass
            # try:
            #     status = strip_tags(phoneScrap.text.split('data-spec="status">')[1].split("</td>")[0])
            # except:
            #     status = ""
            #     pass
            # try:
            #     dimensions = strip_tags(phoneScrap.text.split('data-spec="dimensions">')[1].split("</td>")[0])
            # except:
            #     dimensions = ""
            #     pass
            # try:
            #     weigth = strip_tags(phoneScrap.text.split('data-spec="weight">')[1].split("</td>")[0])
            # except:
            #     weigth = ""
            #     pass
            # try:
            #     sim = strip_tags(phoneScrap.text.split('data-spec="sim">')[1].split("</td>")[0])
            # except:
            #     sim = ""
            #     pass
            # try:
            #     displayType = strip_tags(phoneScrap.text.split('data-spec="displaytype">')[1].split("</td>")[0])
            # except:
            #     displayType = ""
            #     pass
            # try:
            #     displaySize = strip_tags(phoneScrap.text.split('data-spec="displaysize">')[1].split("</td>")[0])
            # except:
            #     displaySize = ""
            #     pass
            # try:
            #     displayResolution = strip_tags(phoneScrap.text.split('data-spec="displayresolution">')[1].split("</td>")[0])
            # except:
            #     displayResolution = ""
            #     pass
            # try:
            #     os = strip_tags(phoneScrap.text.split('data-spec="os">')[1].split("</td>")[0])
            # except:
            #     os = ""
            #     pass
            # try:
            #     chipset = strip_tags(phoneScrap.text.split('data-spec="chipset">')[1].split("</td>")[0])
            # except:
            #     chipset = ""
            #     pass
            # try:
            #     cpu = strip_tags(phoneScrap.text.split('data-spec="cpu">')[1].split("</td>")[0])
            # except:
            #     cpu = ""
            #     pass
            # try:
            #     gpu = strip_tags(phoneScrap.text.split('data-spec="gpu">')[1].split("</td>")[0])
            # except:
            #     gpu = ""
            #     pass
            # try:
            #     memoryslot = strip_tags(phoneScrap.text.split('data-spec="memoryslot">')[1].split("</td>")[0])
            # except:
            #     memoryslot = ""
            #     pass
            # try:
            #     internalmemory = strip_tags(phoneScrap.text.split('data-spec="internalmemory">')[1].split("</td>")[0])
            # except:
            #     internalmemory = ""
            #     pass
            # try:
            #     cam1modules = strip_tags(phoneScrap.text.split('data-spec="cam1modules">')[1].split("</td>")[0])
            # except:
            #     cam1modules = ""
            #     pass
            # try:
            #     cam1features = strip_tags(phoneScrap.text.split('data-spec="cam1features">')[1].split("</td>")[0])
            # except:
            #     cam1features = ""
            #     pass
            # try:
            #     cam1video = strip_tags(phoneScrap.text.split('data-spec="cam1video">')[1].split("</td>")[0])
            # except:
            #     cam1video = ""
            #     pass
            # try:
            #     cam2modules = strip_tags(phoneScrap.text.split('data-spec="cam2modules">')[1].split("</td>")[0])
            # except:
            #     cam2modules = ""
            #     pass
            # try:
            #     cam2features = strip_tags(phoneScrap.text.split('data-spec="cam2features">')[1].split("</td>")[0])
            # except:
            #     cam2features = ""
            #     pass
            # try:
            #     cam2video = strip_tags(phoneScrap.text.split('data-spec="cam2video">')[1].split("</td>")[0])
            # except:
            #     cam2video = ""
            #     pass
            # try:
            #     wlan = strip_tags(phoneScrap.text.split('data-spec="wlan">')[1].split("</td>")[0])
            # except:
            #     wlan = ""
            #     pass
            # try:
            #     bluetooth = strip_tags(phoneScrap.text.split('data-spec="bluetooth">')[1].split("</td>")[0])
            # except:
            #     bluetooth = ""
            #     pass
            # try:
            #     gps = strip_tags(phoneScrap.text.split('data-spec="gps">')[1].split("</td>")[0])
            # except:
            #     gps = ""
            #     pass
            # try:
            #     nfc = strip_tags(phoneScrap.text.split('data-spec="nfc">')[1].split("</td>")[0])
            # except:
            #     nfc = ""
            #     pass
            # try:
            #     radio = strip_tags(phoneScrap.text.split('data-spec="radio">')[1].split("</td>")[0])
            # except:
            #     radio = ""
            #     pass
            # try:
            #     usb = strip_tags(phoneScrap.text.split('data-spec="usb">')[1].split("</td>")[0])
            # except:
            #     usb = ""
            #     pass
            # try:
            #     sensors = strip_tags(phoneScrap.text.split('data-spec="sensors">')[1].split("</td>")[0])
            # except:
            #     sensors = ""
            #     pass
            # try:
            #     batdescription1 = strip_tags(phoneScrap.text.split('data-spec="batdescription1">')[1].split("</td>")[0])
            # except:
            #     batdescription1 = ""
            #     pass
            # try:
            #     colors = strip_tags(phoneScrap.text.split('data-spec="colors">')[1].split("</td>")[0])
            # except:
            #     colors = ""
            #     pass
            # try:
            #     modelss = strip_tags(phoneScrap.text.split('data-spec="models">')[1].split("</td>")[0])
            # except:
            #     modelss = ""
            #     pass
            try:
                price = strip_tags(phoneScrap.text.split('data-spec="price">')[1].split("</td>")[0])
                # price = price.split(';')[-1]
            except:
                price = ""
                pass
            # try:
            #     performance = strip_tags(phoneScrap.text.split('data-spec="tbench">')[1].split("</td>")[0])
            # except:
            #     performance = ""
            #     pass
            # try:
            #     batlife = strip_tags(phoneScrap.text.split('data-spec="batlife">')[1].split("</td>")[0])
            # except:
            #     batlife = ""
            #     pass
            phone = Phone.objects.create(name=name, model=model, price=price)
            return Phone.objects.filter(pk=phone.pk).all()
