
import re
import os

source_path = "/home/joanramon/Documents/M1/Originals/Web/0221_IC10B0 Muntatge i manteniment d'equipsWEB.html"

print(f"Checking file: {source_path}", flush=True)

if not os.path.exists(source_path):
    print("File does not exist!", flush=True)
else:
    print(f"File size: {os.path.getsize(source_path)} bytes", flush=True)
    
    try:
        with open(source_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            print("File read successfully.", flush=True)
            
            # Case-insensitive search for "Tipus de corrent" or "OA2"
            search_terms = ["Tipus de corrent", "OA2", "Lliçó 1"]
            
            for term in search_terms:
                print(f"Searching for '{term}'...", flush=True)
                # content.lower().find(term.lower())
                start_index = content.lower().find(term.lower())
                
                if start_index != -1:
                    print(f"FOUND '{term}' at index {start_index}", flush=True)
                    chunk = content[start_index:start_index + 20000] # Get large chunk
                    
                    # Extract images
                    images = re.findall(r'<img[^>]+src="([^">]+)"', chunk)
                    print(f"--- IMAGES FOUND NEAR '{term}' ---", flush=True)
                    for img in images:
                        print(img, flush=True)
                    print("-----------------------------", flush=True)
                else:
                    print(f"'{term}' NOT FOUND.", flush=True)

    except Exception as e:
        print(f"Error reading file: {e}", flush=True)
