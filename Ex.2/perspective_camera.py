from PIL import Image
from Primitives.ray import *
from Primitives.primitive import *
from image import *
import numpy as np

## Class for othogonal camera
class Camera:

    ## Constructor
    def __init__(self, position = Vec3(0, 0, 0), view_direction = Vec3(0, 0, 1), width = 512, height = 512, near = .1, far = 1000):
        
        ## Position of the camera
        self.position = position
        ## Direction camera is facing
        self.view_direction = view_direction.normalize() # target
        ## Width in pixels
        self.width = width
        ## Height in pixels
        self.height = height
        ## Near clipping plane
        self.near = near
        ## Far clipping plane
        self.far = far
        ## Field of View
        self.fov = 65.0
        ##
        self.up = Vec3(0, 1, 0)

    def adaptive_antialiasing(ray, A, B, C, D, E, depth, maxDepth, horizontal, vertical, background_color, primitives):
        
        ray.set_direction(E)
        eColor = ray.get_color_from_hitable(primitives)

        ray.set_direction(A)
        aColor = ray.get_color_from_hitable(primitives)

        ray.set_direction(B)
        bColor = ray.get_color_from_hitable(primitives)

        ray.set_direction(C)
        cColor = ray.get_color_from_hitable(primitives)

        ray.set_direction(D)
        dColor = ray.get_color_from_hitable(primitives)

        """
        A---B
        |	|
        | E |
        |	|
        D---C
        A, B, C, D, E
        FOR A, E box: A, E + ver, E, E-hor, E-hor/2 + ver/2
        FOR B, E box: E + ver, B, E + hor, E, E + hor/2 + ver/2
        FOR C, E box: E, E+hor, C, E-ver, E + hor/2 - ver/2
        FOR D, E box: E - hor, E, E - ver, D, E-hor/2 - ver/2
        """
        
        # Check if algorithm reached maximum Depth, if so return color of the middle of subpixel
        if (depth >= maxDepth):
        
            return eColor
        

        if (aColor != eColor):
        
            bPrim = E + vertical
            dPrim = E - horizontal
            ePrim = E - horizontal / 2 + vertical / 2
            aColor = Camera.adaptive_antialiasing(ray, A, bPrim, E, dPrim, ePrim, depth + 1, maxDepth, horizontal / 2, vertical / 2, backgroundColor)
        
        if (bColor != eColor):
        
            aPrim = E + vertical
            cPrim = E + horizontal
            ePrim = E + horizontal / 2 + vertical / 2
            bColor = Camera.adaptive_antialiasing(ray, aPrim, B, cPrim, E, ePrim, depth + 1, maxDepth, horizontal / 2, vertical / 2, backgroundColor)
        
        if (cColor != eColor):
        
            bPrim = E + horizontal
            dPrim = E - vertical
            ePrim = E + horizontal / 2 - vertical / 2
            cColor = Camera.adaptive_antialiasing(ray, E, bPrim, C, dPrim, ePrim, depth + 1, maxDepth, horizontal / 2, vertical / 2, backgroundColor)
        
        if (dColor != eColor):
        
            aPrim = E - horizontal
            cPrim = E - vertical
            ePrim = E - horizontal / 2 - vertical / 2
            dColor = Camera.adaptive_antialiasing(ray, aPrim, E, cPrim, D, ePrim, depth + 1, maxDepth, horizontal / 2, vertical / 2, backgroundColor)
        

        # get mean of the colors and return them
        return ((aColor + eColor) * 0.5 + (bColor + eColor) * 0.5 + (cColor + eColor) * 0.5 + (dColor + eColor) * 0.5) * 0.25
    
    
    def render_scene(self, primitives):
        image = MyImage(self.height, self.width)
        image.fancy_background()
        ## Coordinates viewPlane
        w = Vec3(0, 0, 0)
        u = Vec3(0, 0, 0)
        v = Vec3(0, 0, 0)
        theta = self.fov * math.pi / 180
        halfHeight = math.tan( theta / 2.0)
        aspect = self.width / self.height
        halfWidth = aspect * halfHeight
	
	    # nearPlane is used to mark viewFrustrum
        nearPlane = Vec3.length(self.view_direction - self.position)

	    # W, U, V coordinates, V and U are swapped places and v is negated compared to original
        w = Vec3.normalize(self.position - self.view_direction)
        u = Vec3.normalize(-(Vec3.cross(self.up, w)))
        v = Vec3.normalize(Vec3.cross(w, u))
        
        u0 = self.position.x - halfWidth * nearPlane
        v0 = self.position.y - halfHeight * nearPlane

        # lower left corner of ViewPlane
        lowerLeftCorner = u * u0 + v * v0 - nearPlane * w

        # lower right corner of ViewPlane
        horizontal = (2 * halfWidth * nearPlane) * u

        # upper left corner of ViewPlane
        vertical = (2 * halfHeight * nearPlane) * v

        # size of singular pixel in viewPlane
        pixelHorizontal = horizontal / self.width
        pixelVertical = vertical / self.height

        for i in range(self.width):
        
            for j in range(self.height):

            
                # New Ray, direction will be changed in antialiasing
                ray = Ray(self.position, Vec3(0.0, 0.0, 1.0))
                
                # Calculate middle of pixel and  corners of the pixel, A, B, C, D, look at antialiasing for exact positions
                rayTarget = lowerLeftCorner + pixelVertical * j + pixelHorizontal * i + pixelHorizontal / 2 + pixelVertical/ 2
                aCorner = rayTarget - pixelHorizontal / 2 + pixelVertical / 2
                bCorner = rayTarget + pixelHorizontal / 2 + pixelVertical / 2
                cCorner = rayTarget + pixelHorizontal / 2 - pixelVertical / 2
                dCorner = rayTarget - pixelHorizontal / 2 - pixelVertical / 2	

                # Get background color from buffer, used in antialiasing
                backgroundColor = image.get_pixel_color(i, j)
                
                # antialiasing
                #finalColor = backgroundColor
                finalColor = Camera.adaptive_antialiasing(ray, aCorner, bCorner, cCorner, dCorner, rayTarget, 0, 5, pixelHorizontal / 2, pixelVertical / 2, backgroundColor, primitives)
                
                # set pixel color 
                image.set_pixel(i, j, finalColor)
        
        MyImage.save_image(image)
            
        
    