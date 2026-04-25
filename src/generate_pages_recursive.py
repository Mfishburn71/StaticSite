def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entry_list = os.listdir(dir_path_content)
    for i in entry_list:
        source_path = os.path.join(dir_path_content , i)
        dest_path = os.path.join(dest_dir_path , i)
        if os.path.isfile(source_path):
            if source_path[-3:] == ".md":
                html_path = dest_path[:-3] + ".html"
                generate_page(source_path, template_path, html_path)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(source_path, template_path, dest_path)
