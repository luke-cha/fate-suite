import os
import json
from pathlib import Path

def scan_files(root_dir='.'):
    """Scan files and organize them by their parent folder name."""
    file_categories = {}
    target_folders = {'image', 'audio', 'video'}
    
    # Walk through all files in the directory
    for root, _, files in os.walk(root_dir):
        # Get path parts
        path_parts = Path(root).parts
        
        # Find the category by checking each part of the path
        category = None
        for part in path_parts:
            if part.lower() in target_folders:
                category = part.lower()
                break
        
        # If we found a target folder in the path
        if category:
            for file in files:
                # Skip hidden files and .git directory
                if file.startswith('.') or '.git' in root:
                    continue
                
                # Get the full path and make it relative to root_dir
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, root_dir)
                
                # Add file to appropriate category
                if category not in file_categories:
                    file_categories[category] = []
                file_categories[category].append(relative_path)
    
    return file_categories

def main():
    # Scan files
    file_categories = scan_files()
    
    # Sort files within each category
    for category in file_categories:
        file_categories[category].sort()
    
    # Save to JSON file
    output_file = 'file_structure.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(file_categories, f, indent=2, ensure_ascii=False)
    
    print(f"File structure has been saved to {output_file}")

if __name__ == "__main__":
    main() 