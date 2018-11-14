from PIL import Image
import os

#map_image = Image.open("Master_Map.jpg")
#Image._show(map_image)
#map_image.show()
#map_image.save("Master_Map.bmp")
size_300 = (300,300)
size_800 = (800,800)

for file in os.listdir('.'):
    if file.endswith('.bmp'):
        img = Image.open(file)
        fn,fext = os.path.splitext(file)

        img.thumbnail(size_800)
        img.convert(mode='L').save("800\{}_800.jpg".format(fn))
        #img.save("800\{}_800.jpg".format(fn))
        print("{}_800.jpg".format(fn))

        img.thumbnail(size_300)
        img.save("300\{}_300.jpg".format(fn))
        print("{}_300.jpg".format(fn))



#print(os.chdir("."))