from rembg import remove
from PIL import image

input_path = '' # original image archive
output_path = '' # new archive without backgorund

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open('')# new archive name