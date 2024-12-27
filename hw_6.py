class Animal:
    name = None
    species = None
    age = None


    def __init__(self,name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.get_attr()


    def make_sound(self):
        if self.species == 'dog':
            print (f'{self.name} makes a sound: baw ')
        elif self.species == 'cat':
            print(f'{self.name} makes a sound: meow ')


    def get_attr(self):
        print(self.name, 'age:', self.age,'. species:',self.species)

Animal1 =Animal ('Skubby', 'dog', 5)
Animal2 =Animal ('Nana', 'cat', 2)

Animal1.make_sound()
Animal2.make_sound()
print ('--------------')



class Rectangle:
    width = None
    height = None

    def get_attr(self):
        print (self.width, 'width', self.height,'height' )

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.get_attr()

    def calculate_area(self,width, height):
        result = (width * height)
        print (f'The are is {result}')

Rectangle1 = Rectangle(45,80)
Rectangle2 = Rectangle(65,100)

Rectangle1.calculate_area(45, 80)
Rectangle2.calculate_area(65, 100)




