from tkinter.font import names


class Car:

    def __init__(self,o_name,o_engine, o_model):

        self.name = o_name
        self.engine = o_engine
        self.model = o_model

    def start_engine(self):
        print("Starting the car with the name",self.name)
        print("Starting the car with the engine",self.engine)
        print("Starting the car with the model",self.model)

lambo = Car("lamborgini", "V6", "2023")
lambo.start_engine()

mg_hector = Car("mghector", "turbo 1+", "2024")
mg_hector.start_engine()



