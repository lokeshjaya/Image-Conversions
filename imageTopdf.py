from PIL import Image
import os
file_name="text.png"
im=Image.open(file_name)
if im.mode=="RGBA":
    im=im.convert("RGB")
new_file="test.pdf"
if not os.path.exists(new_file):
    im.save(new_file,"PDF",resolution=100.0)