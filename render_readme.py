import re
from os.path import exists, getmtime, join

from jinja2 import BaseLoader, Environment, TemplateNotFound

README_TEMPLATE = "readme_template.md"
GETTING_STARTED_TEMPLATE = "getting_started.md"

with open(join("guides", GETTING_STARTED_TEMPLATE)) as getting_started_file:
    getting_started = getting_started_file.read()

code_tags = re.findall(r'\{\{ code\["([^\s]*)"\] \}\}', getting_started)
demo_tags = re.findall(r'\{\{ demos\["([^\s]*)"\] \}\}', getting_started)
code, demos = {}, {}

for code_src in code_tags:
    with open(join("demo", code_src, "run.py")) as code_file:
        python_code = code_file.read()
        python_code = python_code.replace(
            'if __name__ == "__main__":\n    iface.launch()', "iface.launch()"
        )
        code[code_src] = "```python\n" + python_code + "\n```"

for demo_src in demo_tags:
    demos[demo_src] = (
        "![" + demo_src + " interface](demo/" + demo_src + "/screenshot.gif)"
    )


class GuidesLoader(BaseLoader):
    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
        mtime = getmtime(path)
        with open(path) as f:
            source = f.read()
        return source, path, lambda: mtime == getmtime(path)


readme_template = Environment(loader=GuidesLoader(".")).get_template(README_TEMPLATE)
output_readme = readme_template.render(code=code, demos=demos)
output_readme = output_readme.replace("(/assets/", "(website/homepage/src/assets/")

with open("README.md", "w") as readme_md:
    readme_md.write(output_readme)
