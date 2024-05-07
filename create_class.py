# -*- coding: utf-8 -*-


#Create a class with instance attributes

''' write a python program to create a vehicle class with max_speed and mileage instance attributes'''


class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        
modelX=vehicle(240,18)
print(modelX.max_speed,modelX.mileage)

