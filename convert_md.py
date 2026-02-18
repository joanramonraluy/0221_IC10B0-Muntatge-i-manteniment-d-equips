
import re
import os

SOURCE = 'originals/U1-ll1-oa2.md'
DEST = 'Unitats/Unitat_1_HTML/Llico_1/Llico_1_OA2.html'

# Styles from Llico_1_OA1.html
STYLE_MAIN_DIV = 'line-height: 1.6; text-align: justify;'
STYLE_H3 = 'color: rgb(0, 74, 153); font-family: "Segoe UI", Roboto, sans-serif;'
STYLE_P = 'color: rgb(34, 34, 34); font-family: "Segoe UI", Roboto, sans-serif;'
STYLE_BOX_GRAY = 'color: rgb(34, 34, 34); font-family: "Segoe UI", Roboto, sans-serif; background-color: rgb(247, 247, 247); padding: 10px; border-left: 4px solid rgb(153, 153, 153); margin: 15px 0px;'
STYLE_BOX_BLUE = 'color: rgb(34, 34, 34); font-family: "Segoe UI", Roboto, sans-serif; background-color: rgb(238, 246, 255); padding: 10px; border-left: 4px solid rgb(58, 123, 213); margin: 15px 0px;'
STYLE_FIG = 'text-align: center; margin: 20px 0;'
STYLE_IMG = 'max-width: 100%; border-radius: 8px; border: 1px solid #ddd;'
STYLE_CAP = 'font-size: 0.9em; color: #666; margin-top: 5px;'

def parse_inline(text):
    # Bold **Text** -> <strong>Text</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic *Text* -> <em>Text</em> (Only if not surrounded by other stars presumably, specifically for MD)
    # But simple regex works for well-formed MD
    text = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    return text

def convert():
    if not os.path.exists(SOURCE):
        print(f"Error: Source file {SOURCE} not found.")
        return

    with open(SOURCE, 'r') as f:
        content = f.read()

    # 1. Extract Images
    # Format: [imageN]: <data:image/png;base64,...>
    images = {}
    # Use dotall if needed, but usually these are single line or ends of file
    # The <> wrapper seems to be used.
    img_defs = re.findall(r'^\[(image\d+)\]:\s*<(data:.*)>', content, re.MULTILINE)
    if not img_defs:
        # Try without <> just in case
        img_defs = re.findall(r'^\[(image\d+)\]:\s*(data:.*)', content, re.MULTILINE)
    
    for name, data in img_defs:
        images[name] = data.strip()
    
    print(f"Found {len(images)} images.")

    # 2. Remove image definitions from content to avoid processing them as text
    content_body = re.sub(r'^\[image\d+\]:\s*.*', '', content, flags=re.MULTILINE)
    
    lines = content_body.split('\n')
    
    html_parts = []
    html_parts.append('<!-- 🔷 LLIÇÓ 1 - OA2: TIPUS DE CORRENTS I SENYALS -->')
    html_parts.append(f'<div style="{STYLE_MAIN_DIV}">')
    
    # 3. Add Header (Duration) - Hardcoded based on previous file content
    html_parts.append(f'    <div style="{STYLE_BOX_GRAY}">')
    html_parts.append(f'        🧭 <strong>Durada estimada:</strong> 2 hores')
    html_parts.append(f'    </div>')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
            
        # Headers ####
        if line.startswith('####'):
            # Remove #### and **
            text = line.replace('####', '').strip()
            text = text.replace('**', '').strip() # Clean bold markers in headers
            html_parts.append(f'    <h3 style="{STYLE_H3}">{text}</h3>')
            i += 1
            continue
            
        # Images ![][imageX]
        img_match = re.match(r'!\[\]\[(image\d+)\]', line)
        if img_match:
            img_id = img_match.group(1)
            src = images.get(img_id, '')
            i += 1
            
            # Look ahead for caption
            caption = ""
            while i < len(lines) and not lines[i].strip():
                i += 1 # Skip blank lines
            
            if i < len(lines):
                cap_line = lines[i].strip()
                # Check if it looks like a caption (starts with *)
                if cap_line.startswith('*') and cap_line.endswith('*'):
                    caption = cap_line[1:-1].strip()
                    i += 1
                elif cap_line.startswith('Figura') or cap_line.startswith('Imatge') or cap_line.startswith('Esquema') or cap_line.startswith('Gràfic') or cap_line.startswith('Fotografia') or cap_line.startswith('Pila'):
                     # Heuristic for implicit captions like "Esquema visual..." which might not be italicized in MD
                     caption = cap_line
                     i += 1
            
            html_parts.append(f'    <figure style="{STYLE_FIG}">')
            if src:
                html_parts.append(f'        <img src="{src}" alt="{caption}" style="{STYLE_IMG}">')
            else:
                html_parts.append(f'        <!-- MISSING IMAGE {img_id} -->')
            
            if caption:
                html_parts.append(f'        <figcaption style="{STYLE_CAP}">{parse_inline(caption)}</figcaption>')
            html_parts.append(f'    </figure>')
            continue
            
        # Special Boxes: Metàfora, Exemple
        if line.startswith('🎯') or line.startswith('💡'):
            processed = parse_inline(line)
            html_parts.append(f'    <div style="{STYLE_BOX_BLUE}">')
            html_parts.append(f'        {processed}')
            html_parts.append(f'    </div>')
            i += 1
            continue
            
        # Normal Paragraphs
        processed = parse_inline(line)
        html_parts.append(f'    <p style="{STYLE_P}">{processed}</p>')
        i += 1
        
    html_parts.append('</div>')
    
    final_output = '\n'.join(html_parts)
    
    # Ensure directory exists (it should)
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    
    with open(DEST, 'w') as f:
        f.write(final_output)
    
    print(f"Successfully generated {DEST} size={len(final_output)}")

if __name__ == '__main__':
    convert()
