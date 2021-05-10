## Documentation for a class PointLightSource. Light emitted from a Point.
class PointLightSource(LightSource):

    def getIntensityAt(self, point): 
        distance = (self.location - point).normalize()
        #if (distance < epsilon) :
            #distance = epsilon
        return 1 / (distance * distance)