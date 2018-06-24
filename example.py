from CedarAPI import *

api =CedarAPI('')
forward =api.ForwardGeocoding(term='ونک',limit=2,type='locality,roundabout',distance=12)
print(forward[0]) #results
print(forward[1])  #status
#print(api.ReverseGeocoding('35.716482704636825','51.40897750854492'))