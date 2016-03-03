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


class CarFactory(object):
    def create(self):
        return Car()

class PlaneFactory(object):
    def create(self):
        return Plane()


class VehicleFactory(object):
    def __init__(self, factory):
        """
        abstract_factory is a Abstract Factory
        """
        self.abstract_factory = factory

    def create(self):
        return self.abstract_factory().create()


vehicle_factory = VehicleFactory(CarFactory)
car = vehicle_factory.create()
car.func()
# Car run

vehicle_factory = VehicleFactory(PlaneFactory)
plane = vehicle_factory.create()
plane.func()
# Plane fly
