## Documentation for a class Material.
class LightSource:

    ## The constructor.
    def __init__(self, colour=(1,1,1), location=(1,1,1)):

        ## Colour of light source.
        self.colour = colour

        ## Location of light source.
        self.location = location

    ## Function returning object values in string format.
    def __str__(self):
        return 'LightSource: colour' + str(self.colour) + ', location' + str(self.location) 

