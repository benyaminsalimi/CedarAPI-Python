import requests

__author__='Benyamin.Salimi@gmail.com'
__repository__='https://github.com/benyaminsalimi/Cedar-Python'

class CedarAPI(object):
    def __init__(self,key):
        self.header = {}
        self.header['Authorization'] = 'Bearer '+key
        self.header['user-agent'] = 'Cedar API Python lib'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        self.api_url = 'https://api.cedarmaps.com/v1/'

    def req(self,url,param=None):
        req = requests.get(url=url, headers=self.header, params=param)
        status = req.json()['status']
        try:
            result = req.json()['results']
        except:
            result = req.json()['result']
        return result, status

    def ForwardGeocoding(self,term,limit,distance=None,location=None,type=None,ne=None,
                         sw=None):
        #type locality, roundabout, street, freeway, expressway, boulevard
        param={}
        param['distance']=distance
        param['location']=location #Center point of a nearby search. should be accompanied with distance param
        param['type']= type #Possible values are: locality, roundabout, street, freeway, expressway, boulevard (You can mix types by separating them with commas)
        param['limit']= limit #max 30
        param['distance'] = float(distance) # Unit is km, 0.1 means 100 meters
        param['ne']= ne # ne	lat,lon	Specifies north east of the bounding box - should be accompanied with sw param
        param['sw'] = sw #	lat,lon	Specifies south west of the bounding box - should be accompanied with ne param
        url = self.api_url+'geocode/cedarmaps.streets/'+term

        return self.req(url=url, param=param)

    def ReverseGeocoding(self,lat,lon):
        url = self.api_url +'geocode/cedarmaps.streets/'+ lat + ',' + lon

        return self.req(url)

    def Distance(self,originlat,originlon,destinationlat,destinationlon):
        url = self.api_url + 'distance/cedarmaps.driving/'+ originlat +','+ originlon +';'+ destinationlat +','+ destinationlon
        return self.req(url)

    def Direction(self,originlat,originlon,destinationlat,destinationlon):
        url = self.api_url + 'direction/cedarmaps.driving/'+ originlat +','+ originlon +';'+ destinationlat +','+ destinationlon
        return self.req(url)

    ##TODO:Getting TileJSON