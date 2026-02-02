import os
import base64
import re

# Mapping of HTML filename -> list of (substring_in_alt_or_caption, image_filename)
# Check alt text or just use sequential replacement if we are confident.
# Using sequential replacement based on the verified order.

files_and_images = {
    'Llico_1_OA1.html': [
        'img-001.png', # Analogia tensió
        'img-002.png', # Analogia corrent
        'img-003.png', # Analogia resistència
        'img-004.png', # Etiquetes potència
        'img-005.png'  # Llei Ohm representation
    ],
    'Llico_1_OA2.html': [
        'img-006.png', # Pila
        'img-007.png', # Gràfic DC
        'img-008.png', # Multímetre DC
        'img-009.png', # Gràfic AC
        'img-010.png', # Endoll
        'img-011.png', # Multímetre AC
        'img-012.png', # Ona analògica
        'img-013.png', # Comparativa
        'img-014.png'  # Senyal digital
    ],
    'Llico_1_OA3.html': [
        'img-015.png'  # Triangle Ohm
    ]
}

base_dir = '/home/joanramon/Documents/M1'
html_dir = os.path.join(base_dir, 'Unitats/Unitat_1_HTML')
images_dir = os.path.join(base_dir, 'extracted_images')

def embed_images(html_file, image_list):
    full_path = os.path.join(html_dir, html_file)
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find <img src="...">
    # We will replace them sequentially.
    # Be careful not to replace other images if any (e.g. icons).
    # Assuming all main images are the targets.
    
    # We split by <img src="...
    parts = re.split(r'(<img src="[^"]+")', content)
    
    new_content = ""
    img_idx = 0
    
    for part in parts:
        if part.startswith('<img src="'):
            if img_idx < len(image_list):
                img_name = image_list[img_idx]
                img_path = os.path.join(images_dir, img_name)
                
                if os.path.exists(img_path):
                    with open(img_path, "rb") as img_f:
                        b64_data = base64.b64encode(img_f.read()).decode('utf-8')
                        new_content += f'<img src="data:image/png;base64,{b64_data}"'
                        print(f"Embedded {img_name} into {html_file}")
                else:
                    print(f"Image not found: {img_path}")
                    new_content += part # Keep original if not found
                
                img_idx += 1
            else:
                new_content += part # No more images to embed
        else:
            new_content += part

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

for html_file, images in files_and_images.items():
    embed_images(html_file, images)
