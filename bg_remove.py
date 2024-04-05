from rembg import remove
from PIL import Image
input_path = 'team1.jpg'
output_path = 'team.jpg'

inp = Image.open(input_path)
output = remove(inp)
output = output.convert("RGB")
output.save(output_path)
