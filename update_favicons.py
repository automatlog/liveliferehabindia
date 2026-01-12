import os

root_dir = r"c:\Users\AMAN\Downloads\liveliferehabindia"
# The exact URL found in grep keys
target_url = "https://cdn.prod.website-files.com/683f409fbad13ddc254de956/683f469df40fb091edcea267_Favicon.svg"

count = 0
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(subdir, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if target_url in content:
                    # Calculate relative path depth
                    rel_path = os.path.relpath(filepath, root_dir)
                    # depth is number of separators in relative path
                    # e.g. "index.html" -> 0, "services/foo.html" -> 1
                    depth = rel_path.count(os.sep)
                    
                    if depth == 0:
                        new_href = "images/favicon.png"
                    else:
                        new_href = "../images/favicon.png"
                    
                    new_content = content.replace(target_url, new_href)
                    
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated: {rel_path}")
                    count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated: {count}")
