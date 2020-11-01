class Circle():    
    def __init__(self,radius):
        """
        Instance method initializes circle size with specific radius
        self represents the instance created from the class
        """
        self.radius=radius

    def __str__(self):
        """
        Like toString in Java, this method is called whenever the objects is rendered as string
        """
        return(f'I am a circle with Radius {self.radius}')

    '''
    @classmethod decorate a class into class method. By passing class itself as a positional parameter, you can call from class.
    And, all instances from this class also can call it. It shared by all instances.
    '''
    '''
    @staticmethod change the beharvior of a method, make it same for all instances. e.g. format
    '''
    @property
    def diameter(self):
        '''
        @property change the function to accessible like a property/attribute
        '''
        return self.radius*2
    @diameter.setter
    def diameter(self,diameter):
        '''
        @<propertyName>.setter, the name of the setter method should be the same as the name of the property
        '''
        self.radius=diameter/2


c=Circle(3)
# call __str__ to print the string instead of object description
print(c)
print(c.diameter)
c.diameter=8
print(c)