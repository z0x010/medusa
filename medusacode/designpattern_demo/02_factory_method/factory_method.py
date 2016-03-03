#!/usr/bin/env python
# coding:utf-8


class Vehicle(object):
    def func(self):
        print self.__class__.__name__, 'move'

class Car(Vehicle):
    def func(self):
        print self.__class__.__name__, 'run'

class Plane(Vehicle):
    def func(self):
        print self.__class__.__name__, 'fly'

class VehicleFactory(object):
    def create_vehicle(self, vehicle_type):
        return globals()[vehicle_type]()


vehicle_factory = VehicleFactory()

car = vehicle_factory.create_vehicle('Car')
car.func()
# Car run

plane = vehicle_factory.create_vehicle('Plane')
plane.func()
# Plane fly
