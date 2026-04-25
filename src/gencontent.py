import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown_text):
    for line in markdown_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise Exception("no h1 found")
   


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Doing something when you least expect it! Generating page from {from_path} to {dest_path} using {template_path} in 5 seconds")     
    with open(from_path) as f:
        from_contents = f.read()
    with open(template_path) as f:
        temp_contents = f.read()

    new_contents =markdown_to_html_node(from_contents).to_html()
    new_title = extract_title(from_contents)
    new_file = temp_contents.replace("{{ Title }}", new_title)
    new_file = new_file.replace("{{ Content }}", new_contents)
    new_file = new_file.replace('href="/', 'href="'+basepath)
    new_file = new_file.replace('src="/', 'src="'+basepath)

    ref_path = os.path.dirname(dest_path)
    os.makedirs(ref_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(new_file)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(f"Doing something when you always expect it! Generating pages from {dir_path_content} to {dest_dir_path} using {template_path} in 5 seconds")  
    entry_list = os.listdir(dir_path_content)
    for i in entry_list:
        source_path = os.path.join(dir_path_content , i)
        dest_path = os.path.join(dest_dir_path , i)
        if os.path.isfile(source_path):
            if source_path[-3:] == ".md":
                html_path = dest_path[:-3] + ".html"
                generate_page(source_path, template_path, html_path, basepath)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(source_path, template_path, dest_path, basepath)

