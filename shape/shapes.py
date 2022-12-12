import math as m
import inflect
from configparser import ConfigParser


class Shape(object):
    def __init__(self, color):
        self.color = color
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,color,radius):
        super(Circle, self).__init__(color)
        self.radius = radius

    def area(self):
        C_A =  m.pi*(self.radius^2)
        # print(f"area is {C_A}")
        return C_A

class Square(Shape):
    def __init__(self,color, width, length):
        super(Square, self).__init__(color)
        self.width= width
        self.length=length
    def area(self):
        S_A = self.width*self.length
        # print(S_A)
        return S_A

class Connection(object):

    @staticmethod
    def Config():
        # Read config.ini file
        config_object = ConfigParser()
        try:
            config_object.read("config.ini")
            print("config file read success")
            mono_circle = config_object["Mono-circle"]
            # print("shape is {}".format(MonoCircle["shape"]))
            mono_square = config_object["Mono-square"]
            # print("shape is {}".format(mono_square["shape"]))
            multi_shape = config_object['Multi-shape']
            # print("shape is {}".format(MultiShape["shape"]))
        except:
            print("connection error!! no config.ini file")

        return mono_circle,mono_square,multi_shape


    # # Get the password
    # j=Square(input(),2,4)
    # j.area()

class ConnectedShape(object):
    __circle_connection, __square_connection,__multi_shape = Connection.Config()

    @staticmethod
    def square_only():
        try:
            s = ConnectedShape.__square_connection
            print(f'{ConnectedShape.__square_connection} is connected')
            color = input('input color you want:  ')
            width = input('input width of the square:  ')
            length = input('input length of the square:  ')
            square = Square(color,int(width),int(length))
            s_area = square.area()
            print(f'the {s["shape"]} is {color},and the area is {s_area}')
        except:
            print(f'can not connect {ConnectedShape.__square_connection}')
        return s_area

    @staticmethod
    def circle_only():
        try:
            c = ConnectedShape.__circle_connection
            print(f'{ConnectedShape.__circle_connection} is connected')
            color = input('input color you want:  ')
            radius = input('input radius of the circle:  ')
            circle = Circle(color,int(radius))
            c_area = circle.area()
            print(f'the {c["shape"]} is {color},and the area is {c_area}')
        except:
            print(f'can not connect {ConnectedShape.__circle_connection}')
        return c_area

    @staticmethod
    def multi_shape():
        en = inflect.engine()
        total_Area = 0
        try:
            m = ConnectedShape.__multi_shape
            print(f'{m} is connected')
            number = int(input("pls fill in a number of shapes you want to connect: "))
            if not isinstance(number,int):
                print(f'pls input a number')
            else:
                if number != 0:
                    for i in range(number):
                        j = i + 1
                        first_shape = input(f"pls select the {en.ordinal(j)} shape： ").upper()
                        print(first_shape)
                        if first_shape == 'CIRCLE':
                            c = ConnectedShape.circle_only()
                            total_Area += c
                        elif first_shape == 'SQUARE':
                            s = ConnectedShape.square_only()
                            total_Area += s
                        else:
                            print(f'there is no {first_shape} available')
                            exit(0)
            print(f'the total Area is {total_Area}')
        except:
            print(f'can not connect {ConnectedShape.__multi_shape}')
        return total_Area








