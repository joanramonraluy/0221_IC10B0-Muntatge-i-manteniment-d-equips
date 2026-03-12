import re
import base64
import os

md_path = "/home/joanramon/Documents/M1/originals/Md's/U4/U4-Ll2-OA1 (1h).md"
img_dir = "/home/joanramon/Documents/M1/Unitats/Unitat_4_HTML/Llico_2/img"

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Regular expression to find base64 images
# Format: [image1]: <data:image/png;base64,...>
matches = re.findall(r'\[image(\d+)\]: <data:image/png;base64,(.*?)>', content, re.DOTALL)

for img_num, img_data in matches:
    print(f"Extracting image {img_num}...")
    img_data = img_data.replace("\n", "").replace(" ", "")
    img_bytes = base64.b64decode(img_data)
    img_filename = f"image{img_num}_l2oa1.png"
    img_path = os.path.join(img_dir, img_filename)
    with open(img_path, "wb") as f:
        f.write(img_bytes)
    print(f"Saved to {img_path}")
