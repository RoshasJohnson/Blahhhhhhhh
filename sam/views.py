from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . models import Table, card
from . models import Tabel



# Create your views here.
def home(request):
    item1 = card()
    item1.img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjaoB0YXZCYF7HbSVnhzMaTKFAx54nsWBJlQ&usqp=CAU"
    item1.title ="EIFFEL TOWER"
    item1.dis = "Trance is a 2020 Indian Malayalam language Neo-noir Psychological thriller film directed and produced by Anwar Rasheed and written by Vincent Vadakkan."
    item1.tutn = "100"


    item2 = card()
    item2.img = "https://w0.peakpx.com/wallpaper/543/787/HD-wallpaper-cia-dq-malayalam-film.jpg"
    item2.title ="CIA"
    item2.dis = "Comrade in America (abbreviated as CIA) is a 2017 Indian Malayalam-language action thriller film directed by Amal Neerad, starring Dulquer Salmaan and Karthika Muralidharan in the lead roles."
    item2.tutn = "90"


    item3 = card()
    item3.img = "https://wallpapercave.com/wp/wp6843759.jpg"
    item3.title ="Kali"
    item3.dis = "Kali ( transl. Rage) is a 2016 Indian Malayalam-language action film directed and co-produced by Sameer Thahir."
    item3.tutn = "90"


    item4 = card()
    item4.img = "https://i.pinimg.com/originals/be/1a/6c/be1a6c112c1d495ea33e6ed5843f152b.jpg"
    item4.title = "Kaduva"
    item4.dis = "Kaduva: Directed by Shaji Kailas. With Prithviraj Sukumaran, Vivek Oberoi, Samyuktha Menon, Siddique."
    item4.tutn = "120"

    item = [item1,item2,item3,item4]
    return render(request,'cards.html',{'name':item})

   

# Create your views here.
def table(request):
    t1=Table()
    t1.name='Arjun'
    t1.age = 26
    t1.place='calicut'
    t1.number = 1
    t2=Tabel()
    t2.name='Adarsh'
    t2.age = 20
    t2.place='Pathanamtitta'
    t2.number = 2
    t3=Tabel()
    t3.name='Roshas Johnson'
    t3.age = 19
    t3.place='Kannur'
    t3.number = 3

   
    return render(request,'cards.html',{'Table':[t1,t2,t3]})