from abc import ABC, abstractmethod

class Gearbox(ABC):

    @abstractmethod
    def set_gear(self):
        pass

class Engine(Gearbox):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):    #overriding method for class Engine
        print("Starting")


    def stop(self):     #overriding method for class Engine
        print("Stoping")


    def set_gear(self): #overriding method for class Gearbox
        print("Gearbox is ready")


    def drive(self):
        self.start()
        self.set_gear()
        self.stop()

car_ref = Car()
car_ref.drive()