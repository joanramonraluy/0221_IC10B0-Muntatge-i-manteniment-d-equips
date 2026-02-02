
import re
import os

def split_document_by_units(markdown_path, output_dir):
    """
    Splits a markdown document into separate files based on 'Unitat' headers.
    Headers like '## **Unitat 1' are used as split points.
    """
    
    if not os.path.exists(markdown_path):
        print(f"Error: Markdown file not found at {markdown_path}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Read {len(content)} chars from {markdown_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Regular expression to find Unit headers.
    # It looks for lines starting with '##', optional bolding '**', then 'Unitat'
    # Example: ## **Unitat 1 – ...**
    # We capture the Unit name/number to use in the filename
    
    # Let's verify the header text from previous `head` or `grep` attempts (though they failed).
    # Based on the user's prompt and standard formatting, it's likely "Unitat X".
    # I will split by `^##\s+` and check if the line contains "Unitat".
    
    # Strategy:
    # 1. Split the content by headers that look like Unit headers.
    # 2. The first part is the Index/Intro.
    # 3. Subsequent parts are Units.
    
    # Regex to match the start of a Unit header
    # We use a lookahead to split but keep the delimiter, or just match and handle logic.
    # Pattern: ^(##\s+\*\*?Unitat\s+\d+)
    
    # Actually, simpler: Iterate through lines.
    
    lines = content.splitlines()
    
    current_file_content = []
    current_filename = "Index.md"
    files_created = []
    
    # Regex fix: Handle potential double asterisks **Unitat
    unit_pattern = re.compile(r'^##\s+\**Unitat\s+(\d+)', re.IGNORECASE)
    
    for line in lines:
        match = unit_pattern.match(line)
        if match:
            # Save previous file
            if current_file_content:
                out_path = os.path.join(output_dir, current_filename)
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(current_file_content))
                files_created.append(current_filename)
                print(f"Created {current_filename} ({len(current_file_content)} lines)")
            
            # Start new Unit
            unit_num = match.group(1)
            current_filename = f"Unitat_{unit_num}.md"
            current_file_content = [line] # Start with the header
        else:
            current_file_content.append(line)
            
    # Save the last file
    if current_file_content:
        out_path = os.path.join(output_dir, current_filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(current_file_content))
        files_created.append(current_filename)
        print(f"Created {current_filename} ({len(current_file_content)} lines)")

    # Also need to handle the images reference definitions at the end of the file!
    # They are likely at the very end of the original file.
    # If we split, specific unit files might lose access to these references if they rely on
    # standard markdown reference links [id]: url at the bottom of the *file*.
    # However, I converted them to [id](url) inline?
    # Wait, my replace_images script did: `return f"[{image_id}]: images/{image_filename}"`
    # It replaced the DEFINITION.
    # But where are the USAGES? `![Alt text][image1]`
    # If the usages are scattered, but definitions were at the bottom, they need to be moved to the relevant file
    # OR replicated in all files.
    # Replicating all image definitions in all files is safe and easy.
    
    # Let's extract all image definitions first.
    image_defs = [line for line in lines if re.match(r'^\[image\d+\]:', line)]
    print(f"Found {len(image_defs)} image definitions.")
    
    if image_defs:
        # Append all definitions to every file just to be safe
        for filename in files_created:
            if filename == "Index.md": continue # Index might not need them, but harmless
            
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write('\n\n<!-- Image Definitions -->\n')
                f.write('\n'.join(image_defs))
            print(f"Appended image definitions to {filename}")

if __name__ == "__main__":
    markdown_file = "/home/joanramon/Documents/M1/0221_IC10B0 Muntatge i manteniment d'equips.md"
    output_directory = "/home/joanramon/Documents/M1/Unitats"
    
    print(f"Splitting {markdown_file} into {output_directory}...")
    split_document_by_units(markdown_file, output_directory)
