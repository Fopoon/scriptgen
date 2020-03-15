from json import loads
from os import getcwd
from pathlib import Path
from typing import Dict

from scriptgen import \
    StringBuilder, \
    diff_text, \
    interpolate_text, \
    write_text_file

from scriptgen.templates.markdown import \
    markdown_autogen


def get_text(
    template: str,
    expressions: Dict[str, str],
    timestamp: bool = True
) -> str:
    sb = StringBuilder()
    if timestamp:
        sb.wb(markdown_autogen())
        sb.nl()
    sb.wl(interpolate_text(template, expressions))
    return str(sb)


if __name__ == "__main__":
    cwp = Path(getcwd())

    templates_dir_name = "templates"

    json_path = cwp / templates_dir_name / "VALUES.t.json"
    json_text = json_path.read_text()
    json = loads(json_text)

    templates = {
        (cwp / templates_dir_name / "README.t.md"): (cwp.parent / "README.md"),
        (cwp / templates_dir_name / "CONTRIBUTING.t.md"): (cwp.parent / "CONTRIBUTING.md"),
        (cwp / templates_dir_name / "setup.t.py"): (cwp.parent / "setup.py")
    }

    for template_path, target_path in templates.items():
        template_extension = template_path.suffix
        template_text = template_path.read_text()
        text = get_text(
            template_text,
            json,
            timestamp=(template_extension in [".md"]))
        write_text_file(
            text,
            target_path,
            diff_func=diff_text,
            filter_func=lambda line: line.startswith("[//]: # (Auto-generated"),
            log_func=lambda message: print(message)
        )
