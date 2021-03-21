from django.shortcuts import render
from django.views import View
import joblib
import numpy as np
# Create your views here.



class Carprice(View):

    def get(self,request):
        return render(request,'carprice.html')

    def post(self,request):
        print(request.POST)

        carbrand = request.POST.get('carbrand')
        fueltype = request.POST.get('fueltype')
        aspiration = request.POST.get('aspiration')
        doornumber = request.POST.get('doornumber')
        carbody = request.POST.get('carbody')
        drivewheel = request.POST.get('drivewheel')
        enginelocation = request.POST.get('enginelocation')
        enginetype = request.POST.get('enginetype')
        cylindernumber = request.POST.get('cylindernumber')
        fuelsystem = request.POST.get('fuelsystem')

        carencoding = {
            'alfa-romeo':0 , 'audi':1, 'bmw':2 ,'buick':3, 'chevrolet':4,'dodge':5,'honda':6,'isuzu':7,'jaguar':8,'mazda':9,
            'mercury':10,'mitsubishi':11,'nissan':12,'peugeot':13 ,'plymouth':14,
            'porsche':15, 'renault':16, 'saab':17, 'subaru':18, 'toyota':19, 'volkswagen':20, 'volvo':21
        }

        fueltype_encoding ={
            'gas':1,
            'diesel':0,
        }

        aspiration_encoding ={
            'turbo':1,
            'std':0,
        }

        door_number_encoding ={
            'two':2,
            'four':4,
        }

        drivewheel_encoding ={
            '4wd':0,
            'fwd':1,
            'rwd' : 2,
        }

        engine_location_encoding ={
            'front':0,
            'rear':1,
        }
        
        cylinder_number_encoding ={
            'two':2,
            'three':3,
            'four':4,
            'five':5,
            'six':6,
            'eight':8,
            'twelve':12,
        }

        carbodyencoding={
            'sedan':0,
            'hardtop':0,
            'hatchback':0,
            'wagon':0,
        }
        
        engtype = {
            'ohc':0,
            'ohcf':0,
            'ohcv':0,
            'l':0,
            'dohc':0,
            'rotor':0,
        }

        fuelsys = {
            'mpfi' : 0,
            '2bbl' : 0,
            'mfi' : 0,
            '1bbl' : 0,
            '4bbl' : 0,
            'idi' : 0,
            'spdi' : 0,

        }



        symboling = int(request.POST.get('symboling'))
        wheelbase = float(request.POST.get('wheelbase'))
        carlength = float(request.POST.get('carlength'))
        carwidth = float(request.POST.get('carwidth'))
        carheight = float(request.POST.get('carheight'))
        curbweight = int(request.POST.get('curbweight'))
        enginesize = int(request.POST.get('enginesize'))
        boreratio = float(request.POST.get('boreratio'))
        stroke = float(request.POST.get('stroke'))
        compression = float(request.POST.get('compression'))
        horsepower = int(request.POST.get('horsepower'))
        peakrpm = int(request.POST.get('peakrpm'))
        highwaympg = int(request.POST.get('highwaympg'))
        print(request.POST.get('highwaympg'))


        fuelsys[fuelsystem] = 1
        carbodyencoding[carbody] = 1
        engtype[enginetype] = 1

        cararea = carlength * carwidth * carheight

        max_area = 846007.65
        min_area = 452643.155

        
        cararea = (cararea - min_area)/(max_area-min_area)
        


        test = [symboling,carencoding[carbrand],fueltype_encoding[fueltype],aspiration_encoding[aspiration],door_number_encoding[doornumber],drivewheel_encoding[drivewheel],engine_location_encoding[enginelocation],wheelbase,curbweight,cylinder_number_encoding[cylindernumber],enginesize,boreratio,stroke,compression,horsepower,peakrpm,highwaympg,carbodyencoding['hardtop'],carbodyencoding['hatchback'],carbodyencoding['sedan'],carbodyencoding['wagon'],engtype['dohc'],engtype['l'],engtype['ohc'],engtype['ohcf'],engtype['ohcv'],engtype['rotor'],fuelsys['1bbl'],fuelsys['2bbl'],fuelsys['4bbl'],fuelsys['idi'],fuelsys['mfi'],fuelsys['mpfi'],fuelsys['spdi'],cararea]
        x = np.array(test)
        x = np.reshape(test,(1,-1))
        print(x)
        

        dbfile = open(r'D:\Sourav\Projects\Car Price Detection\carprice\models\finalModel', 'rb')      
        model = joblib.load(dbfile)
        price = model.predict(x)[0]
        price = round(price,2)
        data = {

            'carbrand' : carbrand,
            'fueltype' : fueltype,
            'aspiration' : aspiration,
            'doornumber' : doornumber,
            'carbody' : carbody,
            'drivewheel' : drivewheel,
            'enginelocation' : enginelocation,
            'enginetype' : enginetype,
            'cylindernumber' : cylindernumber,
            'fuelsystem' : fuelsystem,
            'symboling' : symboling,
            'wheelbase' : wheelbase,
            'carlength' : carlength,
            'carwidth' : carwidth,
            'carheight' :carheight,
            'curbweight' : curbweight,
            'enginesize' : enginesize,
            'boreratio' : boreratio,
            'stroke' : stroke,
            'compression' : compression,
            'horsepower' : horsepower,
            'peakrpm' : peakrpm,
            'highwaympg' : highwaympg,
            'price' : price,
        }





        
        return render(request,'carprice.html',data)