from rembg import remove
from PIL import Image #pillow 
input_path = 'team1.jpg'
output_path = 'team.jpg'

inp = Image.open(input_path)
output = remove(inp)
output = output.convert("RGB") #error raised if we do not convert encoding to RGB.
output.save(output_path)
#in an image, background is considered the blurred parts, as main object is the one in focus.
