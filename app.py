from PIL import Image

image = Image.open("you're image")
image = image.convert('L')
w,h = image.size
ratio = h/w
new_w =  90
new_h = int(new_w * ratio)
image = image.resize((new_w,new_h))
ascii_char ='@_#*+=-:.a '


pixels = image.getdata()
char ="".join(ascii_char[pixel//25] for pixel in pixels)
pixel_count = len(char)  
ascii_image = "\n".join([char[index:(index+new_w)] for index in range(0, pixel_count, new_w)])

print(ascii_image)



