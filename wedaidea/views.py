from django.shortcuts import render, redirect
from  django.contrib.auth.models import User
from datetime import datetime
from .models import Image, Report


from django.contrib.auth import authenticate, login


from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)

from base64 import b64decode




import json
import requests

import os
import time

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return render(request, 'user.html')
        else:
        # Return an 'invalid login' error message.
            return render(request, 'system.html')


def system(request):
    return render(request, 'system.html')


def user(request):
    return render(request, 'user.html')


def register(request): #หน้า index.html
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        request_data = request.POST
        username = str(request_data.get('username', None))
        first_name = str(request_data.get('first_name', None))
        last_name = str(request_data.get('last_name', None))
        email = str(request_data.get('email', None))
        password = str(request_data.get('password', None))
        repassword = str(request_data.get('repassword', None))

        user=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
            )
        print(username)
        user.save()
    return render(request, 'user.html')
    

def upload(request): #หน้า index.html
  
    return render(request, 'upload.html')



def download(request): #หน้า index.html
  
    return render(request, 'download.html')



def bad(request): #หน้า bad
    if request.method == 'POST':
        print(request.POST)
        Customer_number = request.POST['Customer_number']
        
        Circuit = request.POST['subject']
        Accessory = request.POST['topic']
        Case = request.POST['chapter']
        f_image = request.FILES['image']

        
        print(type(f_image))
        print(f_image)

        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]
        



        #115KV สายดิน
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="ขาด":
            Accessory = "GR"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="หย่อน":
            Accessory = "GR"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="เป็นสนิม":
            Accessory = "GR"
            Case ="13"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="จุดสนิม":
            Accessory = "GR"
            Case ="14"
        
        #115KV ลูกถ้วย
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="แตก/บิ่น":
            Accessory = "IN"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="แฟลช":
            Accessory = "IN"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="แตกลาย":
            Accessory = "IN"
            Case ="13"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="เปลี่ยนสี":
            Accessory = "IN"
            Case ="14"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="คราปสกปรก":
            Accessory = "IN"
            Case ="15"

        #115KV สายไฟ
        if  Circuit == "115KV" and Accessory == "สายไฟ" and Case =="สายแตก":
            Accessory = "LI"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "สายไฟ" and Case =="คลายตัว":
            Accessory = "LI"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "สายไฟ" and Case =="อุปกรณ์จับสายชำรุด":
            Accessory = "LI"
            Case ="13"

        #115KV จุดต่อ            
        if  Circuit == "115KV" and Accessory == "จุดต่อ" and Case =="เปลี่ยนสี/เป็นสนิม":
            Accessory = "CO"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "จุดต่อ" and Case =="มีรอยอาร์ด":
            Accessory = "CO"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "จุดต่อ" and Case =="บิดงอเสียรูป":
            Accessory = "CO"
            Case ="13"

        #115KV อุปกรณ์ตัดตอน  
        if  Circuit == "115KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="บิน":
            Accessory = "DS"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="แตก":
            Accessory = "DS"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="มีรอยอาร์ค":
            Accessory = "DS"
            Case ="13"



        #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="ขาด":
            Accessory = "GR"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="หย่อน":
            Accessory = "GR"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="เป็นสนิม":
            Accessory = "GR"
            Case ="33"
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="จุดต่อหลวม":
            Accessory = "GR"
            Case ="34"


        #33KV ลูกถ้วย
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="แตก/บิ่น":
            Accessory = "IN"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="แฟลช":
            Accessory = "IN"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="แตกลาย":
            Accessory = "IN"
            Case ="33"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="เปลี่ยนสี":
            Accessory = "IN"
            Case ="34"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="คราปสกปรก":
            Accessory = "IN"
            Case ="35"
        
        #33KV สายไฟ
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="สายแตก":
            Accessory = "LI"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="คลายตัว":
            Accessory = "LI"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="อุปกรณ์จับสายชำรุด":
            Accessory = "LI"
            Case ="33"

        #33KV จุดต่อ
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="เปลี่ยนสี/เป็นสนิม":
            Accessory = "CO"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="มีรอยอาร์ด":
            Accessory = "CO"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="บิดงอเสียรูป":
            Accessory = "CO"
            Case ="33"


         #33KV ล่อฟ้า
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="บิ่นแตก/แตก/ฉีก":
            Accessory = "LA"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="มีรอยอาร์ค":
            Accessory = "LA"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="ผิวสกปรก":
            Accessory = "LA"
            Case ="33"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="เปลี่ยนสี":
            Accessory = "LA"
            Case ="34"

         #33KV คาปาซิเตอร์
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="บิ่น/แตก":
            Accessory = "CA"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="มีรอยอาร์ค":
            Accessory = "CA"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="ผิวสกปรก":
            Accessory = "CA"
            Case ="33"


        #22 KV สายดิน
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="ขาด":
            Accessory = "GR"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="หย่อน":
            Accessory = "GR"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="เป็นสนิม":
            Accessory = "GR"
            Case ="33"
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="จุดต่อหลวม":
            Accessory = "GR"
            Case ="34"


        #22 KV ลูกถ้วย
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="แตก/บิ่น":
            Accessory = "IN"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="แฟลช":
            Accessory = "IN"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="แตกลาย":
            Accessory = "IN"
            Case ="33"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="เปลี่ยนสี":
            Accessory = "IN"
            Case ="34"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="คราปสกปรก":
            Accessory = "IN"
            Case ="35"
        
        #22 KV สายไฟ
        if  Circuit == "22KV" and Accessory == "สายไฟ" and Case =="สายแตก":
            Accessory = "LI"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "สายไฟ" and Case =="คลายตัว":
            Accessory = "LI"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "สายไฟ" and Case =="อุปกรณ์จับสายชำรุด":
            Accessory = "LI"
            Case ="33"

        #22 KV จุดต่อ
        if  Circuit == "22KV" and Accessory == "จุดต่อ" and Case =="เปลี่ยนสี/เป็นสนิม":
            Accessory = "CO"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "จุดต่อ" and Case =="มีรอยอาร์ด":
            Accessory = "CO"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "จุดต่อ" and Case =="บิดงอเสียรูป":
            Accessory = "CO"
            Case ="33"


         #22 KV ล่อฟ้า
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="บิ่นแตก/แตก/ฉีก":
            Accessory = "LA"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="มีรอยอาร์ค":
            Accessory = "LA"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="ผิวสกปรก":
            Accessory = "LA"
            Case ="33"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="เปลี่ยนสี":
            Accessory = "LA"
            Case ="34"

         #22 KV คาปาซิเตอร์
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์" and Case =="บิ่น/แตก":
            Accessory = "CA"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์" and Case =="มีรอยอาร์ค":
            Accessory = "CA"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์" and Case =="ผิวสกปรก":
            Accessory = "CA"
            Case ="33"


       #timedate & time in Python

        timestr = time.strftime("%Y%m%d-%H%M%S")


        f_image.name = "{}_{}_{}_{}_{}{}".format(Customer_number, Circuit, Accessory, Case, timestr, ext)
        print(f_image.name)


        #past image
        pathimage = "/media/{}".format(f_image.name) 
        print(pathimage)


        # UP image cload
        uploaded_file = request.FILES['image']
        print(uploaded_file)
        payload=uploaded_file
        headers = {
        'Content-Type': 'image/jpg'
        }
        path_file = f_image.name

        url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


        response = requests.request("PUT", url, headers=headers, data=payload)

        pathoraclecloud = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)


        ## save ข้อมูลลง ฐานข้อมูล 
        img = Image(Customer_number=Customer_number, Accessory=Accessory, Case=Case, Circuit=Circuit, pathimage=pathimage, pathoraclecloud=pathoraclecloud, image=f_image)
        img.save()
        
        context={'data':{'Customer_number':Customer_number, 'Accessory':Accessory, 'Case':Case, 'Circuit':Circuit, 'pathimage':pathimage, 'pathoraclecloud':pathoraclecloud, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        
        return render(request,'index.html', context=context)
    return render(request, 'bad.html')



def good(request): #หน้า good
    if request.method == 'POST':
        print(request.POST)
        Customer_number = request.POST['Customer_number']
        # Office = request.POST['Pea']
        Circuit = request.POST['subject']
        Accessory = request.POST['topic']
       
        f_image = request.FILES['image']

        # Add เปลี่ยนชื่อ รูป

        print(type(f_image))
        print(f_image)

        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]


        #115KV สายดิน
        if  Circuit == "115KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR10"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN10"
        if  Circuit == "115KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI10"
        if  Circuit == "115KV" and Accessory == "สายดิน":
            Accessory = "CO"
            Case ="CO10"
        if  Circuit == "115KV" and Accessory == "สายดิน":
            Accessory = "DS"
            Case ="DS10"




        #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR30"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN30"
        if  Circuit == "33KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI30"
        if  Circuit == "33KV" and Accessory == "จุดต่อ":
            Accessory = "CO"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า":
            Accessory = "LA"
            Case ="DS30"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์":
            Accessory = "CA"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "อุปกรณ์ตัดตอน":
            Accessory = "DS"
            Case ="DS30"


         #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR30"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN30"
        if  Circuit == "33KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI30"
        if  Circuit == "33KV" and Accessory == "จุดต่อ":
            Accessory = "CO"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า":
            Accessory = "LA"
            Case ="LA30"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์":
            Accessory = "CA"
            Case ="CA30"
        if  Circuit == "33KV" and Accessory == "อุปกรณ์ตัดตอน":
            Accessory = "DS"
            Case ="DS30"


        #22KV สายดิน
        if  Circuit == "22KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR20"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN20"
        if  Circuit == "22KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI20"
        if  Circuit == "22KV" and Accessory == "จุดต่อ":
            Accessory = "CO"
            Case ="CO20"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า":
            Accessory = "LA"
            Case ="LA20"
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์":
            Accessory = "CA"
            Case ="CA22"
        if  Circuit == "22KV" and Accessory == "อุปกรณ์ตัดตอน":
            Accessory = "DS"
            Case ="DS22"


       

        #timedate & time in Python

        timestr = time.strftime("%Y%m%d-%H%M%S")

        
        f_image.name = "{}_{}_{}_{}_{}{}".format(Customer_number, Circuit, Accessory, Case, timestr, ext)
        print(f_image.name)

        
        #past image 
        pathimage = "/media/{}".format(f_image.name) 
        print(pathimage)

        # UP image cload
        uploaded_file = request.FILES['image']
        print(uploaded_file)
        payload=uploaded_file
        headers = {
        'Content-Type': 'image/jpg'
        }
        path_file = f_image.name

        url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


        response = requests.request("PUT", url, headers=headers, data=payload)

            
        pathoraclecloud = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)


        ## save ข้อมูลลง ฐานข้อมูล 
        img = Image(Customer_number=Customer_number, Accessory=Accessory, Case=Case, Circuit=Circuit, pathimage=pathimage, pathoraclecloud=pathoraclecloud, image=f_image)
        img.save()
        
        context={'data':{'Customer_number':Customer_number, 'Accessory':Accessory, 'Case':Case, 'Circuit':Circuit, 'pathimage':pathimage, 'pathoraclecloud':pathoraclecloud, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        return render(request,'index.html', context=context)
    return render(request, 'good.html')



def download(request):
    # if request.method == 'GET':
    #     image = request.POST['username']

    return render(request, 'download.html')
    

def uploadPage(request):
    # if request.method == 'GET':
    #     image = request.POST['username']

    return render(request, 'uploadPage.html')





def uploadPage(request):
    return render(request, 'uploadPage.html')


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def uploadPhoto(request):
    print('function upload photo')
    try:
        header = request.headers
        data = json.loads(str(request.body, encoding='utf-8'))
        print(data)
        b64 = data['b64']
        path_file = '%2June2021%2TestFileName1.jpg'
        url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file
        payload = b64decode(b64, validate=True)
        headers = {
            'Content-Type': 'application/jpg'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        return_json = {"detail": "Upload file successfully"}
        return Response(return_json, status.HTTP_200_OK)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def uploadPage2(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        print(uploaded_file)
        payload=uploaded_file
        headers = {
        'Content-Type': 'image/jpg'
        }
        path_file = "touch.jpg"

        url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


        response = requests.request("PUT", url, headers=headers, data=payload)

        return redirect(uploadPage2)

    return render(request, 'uploadPage2.html')




def report(request):
    if request.method == 'POST':
        print(request.POST)
        Partner = request.POST['Partner']
        Zpm4 = request.POST['Zpm4']
        Powerstation = request.POST['Powerstation']

        f_image = request.FILES['image']



        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]

        timestr = time.strftime("%Y%m%d-%H%M%S")
        f_image.name = "{}_{}{}".format(Zpm4, timestr, ext)
        print(f_image.name)

        pathoraclecloud = "https://objectstorage.ap-tokyo-1.oraclecloud.com/n/peacloud/b/Aidea/o/static%2Fpdf%2Foutput{}.pdf".format(Zpm4)

        
        ## save ข้อมูลลง ฐานข้อมูล 
        img = Report(Partner=Partner, Zpm4=Zpm4, Powerstation=Powerstation, pathoraclecloud=pathoraclecloud, image=f_image)
        img.save()

        from GPSPhoto import gpsphoto
        # Get the data from image file and return a dictionary #อ่านค่าlatlong 
        inputimage = "media/{}".format(f_image.name)
        print(inputimage)
        data = gpsphoto.getGPSData(inputimage)
        latlong = data['Latitude'], data['Longitude']
        print(data['Latitude'], data['Longitude'])
        print(latlong)






        def colr(x, y, z):
            return (x/255, y/255, z/255)
        import reportlab
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen.canvas import Canvas
        from reportlab.lib.utils import ImageReader
        from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Image, Spacer, Frame, Paragraph
        from reportlab.platypus.tables import Table
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
        styles = getSampleStyleSheet()
        styleN = styles["BodyText"]
        styleN.alignment = TA_LEFT
        width, height = A4
        
        f_image = "media/{}".format(f_image.name)
        logo = f_image
        elements = []
        print(f'Height={height}')
        imgw = imgh = 100
        im = Image(logo, width=imgw, height=imgh)
        im.hAlign = 'LEFT'
        elements.append(im)


        headstyle = ParagraphStyle(
            name='MyHeader',
            fontName='Helvetica-Bold',
            fontSize=16,
            leading =10
        )
        doctorstyle = ParagraphStyle(
            name='MyDoctorHeader',
            fontName='Helvetica',
            fontSize=13,
            leading =10
        )
        data = [[Paragraph("TOUCHAVIN", style = headstyle)], [Paragraph("SUPHNOTO", style = doctorstyle)], [Paragraph("PEA", style = doctorstyle)], [Paragraph("Registration No. 505742 ", style = doctorstyle)]]
        elements.append(Table(data, repeatRows=0))
        line1 = ("Name", "Test", "Date", "TIME")
        line2 = ("TOUCHAVIN.", "1","Date", timestr)
        
        data=[line1,line2]
        patientdetailstable = Table(data)
        patientdetailstable.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (4, 0), '#CFEAD4'),
            ('BACKGROUND', (0, 2), (4, 2), '#CFEAD4'),
            ('BOX',(0,0),(-1,-1), 0.5, '#CFEAD4'),
            ('GRID',(0,0),(-1,-1), 0.5, colr(12, 43, 8)),
        ]))
        elements.append(patientdetailstable)
        elements.append(Spacer(1, 20))
        # We use paragraph style because we need to wrap text. We cant directly wrap cells otherwise
        line1 = ["ZPM04", "DEVICETYPE" , "WAYOUT", "CONDITION", "LOCATION", "NOTE"]
        #ตัวแปรในตาราง
        drug1 = Paragraph('{}'.format(Zpm4), styleN)
        drug2 = Paragraph('{}'.format(Powerstation), styleN)
        # drug3 = Paragraph('{}'.format(WAYOUT), styleN)
        # drug4 = Paragraph('{}'.format(DEVICETYPE), styleN)
        drug5 = Paragraph('{}'.format(latlong), styleN)
        # drug6 = Paragraph('{}'.format(NOTE), styleN)
      
        line2 = [drug1, drug2, "Test", "Test", drug5, timestr]
        line3 = ["2", drug1, "1 Tab", "1-0-1", "5 days", ""]
      
        data=[line1,line2, line3]
        for i in range(3,5):
            temp = [str(i), "Some Drug here", "5 ml", "1-0-1", "10 days", "No comments"]
            data.append(temp)

        medstable = Table(data, repeatRows=1)
        medstable.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1), 'TOP'),
            ('TEXTCOLOR',(0,0),(-1,0),colors.white),
            ('BACKGROUND', (0, 0), (-1, 0), colr(40, 196, 15)),
            ('GRID',(0,1),(-1,-1), 0.5, '#CFEAD4'),
                                    ]))
        elements.append(medstable)
        doc = SimpleDocTemplate('static/pdf/output{}.pdf'.format(Zpm4), pagesize=A4, rightMargin=20, leftMargin=20, \
            topMargin=20, bottomMargin=20, allowSplitting=1,\
            title="Prescription", author="MyOPIP.com")
        doc.build(elements)

        # อัพโหลดเข้าcloud
        
        uploaded_file = 'static/pdf/output{}.pdf'.format(Zpm4)
        file = open(uploaded_file,'rb')   #เปิดไฟล์ pdfแล้วส่งค่าไปเก็บตัวแปร อัพเข้า cloud
        payload=file
        headers = {
                'Content-Type': 'application/pdf'
        }

        path_file = 'static/pdf/output{}.pdf'.format(Zpm4)

        url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


        response = requests.request("PUT", url, headers=headers, data=payload)
        file.close()
        
        
        

        return render(request, 'login.html')
    return render(request, 'report.html')