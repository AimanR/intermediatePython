#!/usr/bin/env python3

# 3
# inheritance

class vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color
        
    def filluptank(self):
        self.gas = 100
        
    def emptytank(self):
        self.gas = 0
    
    def gasleft(self):
        return self.gas
    

class car(vehicle):
    def __init__(self,price,gas,color,speed):
        super().__init__(price, gas, color)
        self.speed = speed
        
    def beep(self):
        print('beep beep')
        

class truck(vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
        
    def beep(self):
        print('honk honk')
    
        
bmw = car('1M',100,'red',200)
terak = truck('2k',100,'black',120)

bmw.beep()
terak.beep()