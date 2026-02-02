import os
import base64
import re

def embed_images_in_html(html_file, images_dir):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all src="images/imageX.png"
    # Regex to capture the filename
    matches = re.findall(r'src="(images/([^"]+))"', content)
    
    new_content = content
    
    for full_match, filename in matches:
        image_path = os.path.join(images_dir, filename)
        
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                # determine mime type based on extension
                ext = filename.split('.')[-1].lower()
                mime_type = "image/png" if ext == "png" else "image/jpeg"
                if ext == "gif": mime_type = "image/gif"
                
                b64_data = base64.b64encode(img_file.read()).decode('utf-8')
                data_uri = f"data:{mime_type};base64,{b64_data}"
                
                # Replace in content
                new_content = new_content.replace(full_match, data_uri)
                print(f"Embedded {filename} into {html_file}")
        else:
            print(f"Warning: Image not found: {image_path}")

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

base_dir = '/home/joanramon/Documents/M1'
images_dir = os.path.join(base_dir, 'images')
html_dir = os.path.join(base_dir, 'Unitats/Unitat_1_HTML')

files_to_process = [
    'Llico_1_OA1.html',
    'Llico_1_OA2.html',
    'Llico_1_OA3.html'
]

for html_filename in files_to_process:
    full_path = os.path.join(html_dir, html_filename)
    if os.path.exists(full_path):
        embed_images_in_html(full_path, images_dir)
    else:
         print(f"File not found: {full_path}")
