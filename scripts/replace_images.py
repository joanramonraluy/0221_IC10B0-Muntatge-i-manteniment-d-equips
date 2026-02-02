
import re
import os

def replace_images(markdown_path, images_dir):
    """
    Replaces embedded base64 images in a markdown file with relative paths
    to external image files, assuming image file names match the reference IDs.
    """
    
    if not os.path.exists(markdown_path):
        print(f"Error: Markdown file not found at {markdown_path}")
        return

    if not os.path.exists(images_dir):
        print(f"Error: Images directory not found at {images_dir}")
        return

    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"File read successfully. Size: {len(content)} characters.")
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # More flexible regex
    # Matches [image123]: <data:image... or [image123]: data:image...
    # Case insensitive for 'image' in key? No, usually lowercase.
    pattern = re.compile(r'^\[(image\d+)\]:\s*<?data:image/[^>\n]+>?', re.MULTILINE)
    
    # Debug: find one match
    match = pattern.search(content)
    if match:
        print(f"Debug: Found at least one match: {match.group(0)[:50]}...")
    else:
        print("Debug: No matches found with regex.")
        # Print a sample of what looks like a reference
        sample = re.search(r'\[image\d+\]:', content)
        if sample:
            print(f"Debug: Found potential key: {sample.group(0)}")
            start = sample.start()
            print(f"Debug: Context: {content[start:start+100]}")

    replacement_count = 0
    missing_images = []

    def replacement_func(match):
        nonlocal replacement_count
        image_id = match.group(1)
        image_filename = f"{image_id}.png"
        image_path = os.path.join(images_dir, image_filename)
        
        # Verify if the image file exists
        if os.path.exists(image_path):
            replacement_count += 1
            # Relative path for markdown: images/image123.png
            return f"[{image_id}]: images/{image_filename}"
        else:
            missing_images.append(image_id)
            return match.group(0) # Return original string if image missing

    new_content = pattern.sub(replacement_func, content)

    if replacement_count > 0:
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Replaced {replacement_count} embedded images.")
    else:
        print("No image replacements made.")

    if missing_images:
        print(f"Warning: {len(missing_images)} referenced images were not found in {images_dir}:")
        print(missing_images[:10])

if __name__ == "__main__":
    markdown_file = "/home/joanramon/Documents/M1/0221_IC10B0 Muntatge i manteniment d'equips.md"
    images_directory = "/home/joanramon/Documents/M1/images"
    
    print(f"Processing {markdown_file}...")
    replace_images(markdown_file, images_directory)
