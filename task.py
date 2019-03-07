import os
from datetime import datetime

from markdown2 import markdown as md
from jinja2 import Environment, FileSystemLoader, PackageLoader




BASE_DIR = os.getcwd()
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

def get_md_posts():
    for entry in os.scandir(CONTENT_DIR):
        if all([
            not entry.name.startswith('.'),
            entry.name.endswith('.md'),
            entry.is_file()
        ]):
            yield entry.name


def generate_html(files):
    posts = {}

    for file in files:
        with open(os.path.join(CONTENT_DIR, file)) as f:
            posts[file] = md(f.read(), extras=['metadata'])

    posts = {
        post: posts[post] for post in sorted(posts, key=lambda post: datetime.strptime(posts[post].metadata['date'], '%Y-%m-%d'), reverse=True)
    }

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    home_template = env.get_template('home.html')
    post_template = env.get_template('post-detail.html')

    index_posts_metadata = [posts[post].metadata for post in posts]

    index_html_content = home_template.render(posts=index_posts_metadata)


    with open(os.path.join(OUTPUT_DIR, 'home.html'), 'w') as f:
        f.write(index_html_content)

    # print(index_html_content)

    for post in posts:
        post_metadata = posts[post].metadata

        post_data = {
            'content': posts[post],
            'title': post_metadata['title'],
            'date': post_metadata['date'],
        }

        post_html_content = post_template.render(post=post_data)

        post_file_path = 'output/posts/{slug}/home.html'.format(slug=post_metadata['slug'])

        os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
        with open(post_file_path, 'w') as file:
            file.write(post_html_content)



def main():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    generate_html(get_md_posts())


if __name__ == '__main__':
    main()
