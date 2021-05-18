import math


## Documentation for a class Material.
class Material:

    ## The constructor.
    def __init__(self, ambientColour=(1,1,1), diffuseColour=(1,1,1), reflectColour=(1,1,1), specularColour=(0,0,0), specularExponent=1, mirror_reflection_coefficient=1, diffuse_reflection_coefficient=1, texture=None, refractive_index=1):

        ## Colour of Material under white ambient light. Usually, but not always, the same as diffuseColour.
        self.ambientColour = ambientColour

        ## Colour of Material under direct white light. Usually, but not always, the same as ambientColour.
        self.diffuseColour = diffuseColour

        ## Colour of reflected rays under direct white light. If this is zero then there are no reflections.
        self.reflectColour = reflectColour

        ## Colour of Material's specular highlights. If this is zero then there are no highlights.
        self.specularColour = specularColour

        ## 'Hardness' of Material's specular hightlights - high values give small, sharp highlights.
        self.specularExponent = specularExponent

        self.mirror_reflection_coefficient = mirror_reflection_coefficient
        self.diffuse_reflection_coefficient = diffuse_reflection_coefficient

        self.texture = texture

        self.refractive_index = refractive_index

    ## Function returning object values in string format.
    def __str__(self):
        return 'Material: ambColour' + str(self.ambientColour) + ', diffColour' + str(self.diffuseColour) + ', reflColour' + str(self.reflectColour) \
             + ', specularColour' + str(self.specularColour) + ', specularExponent = ' + str(self.specularExponent) + ', texture = ' + str(self.texture)