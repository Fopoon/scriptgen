from json import loads
from pathlib import Path
from typing import Dict

from scriptgen import \
    StringBuilder, \
    diff_text, \
    interpolate_text, \
    write_text_file


def get_text(
    template: str,
    expressions: Dict[str, str],
    template_name: str = None
) -> str:
    sb = StringBuilder()

    # Add a timestamp when the template is a markdown file.
    if template_name.casefold().endswith(".md"):
        from scriptgen.templates.markdown import markdown_autogen
        sb.wb(markdown_autogen())
        sb.nl()

    # Replace placeholders.
    # i.e. replace placeholders found in the text with values found in the expressions dictionary.
    # ex: ${SOME_KEY} → ACTUAL_VALUE
    interpolated_text = interpolate_text(template, expressions)

    # Write the interpolated text into the builder.
    sb.wl(interpolated_text)

    return str(sb)


if __name__ == "__main__":
    fdp = Path(__file__).parent

    templates_dir_name = "templates"

    # scriptgen/tools/templates/VALUES.t.json
    json_path = fdp / templates_dir_name / "VALUES.t.json"
    json_text = json_path.read_text()
    json = loads(json_text)

    templates = {
        # scriptgen/tools/templates/README.t.md → scriptgen/README.md
        (fdp / templates_dir_name / "README.t.md"): (fdp.parent / "README.md"),
        # scriptgen/tools/templates/CONTRIBUTING.t.md → scriptgen/CONTRIBUTING.md
        (fdp / templates_dir_name / "CONTRIBUTING.t.md"): (fdp.parent / "CONTRIBUTING.md"),
        # scriptgen/tools/templates/setup.t.py → scriptgen/setup.py
        (fdp / templates_dir_name / "setup.t.py"): (fdp.parent / "setup.py")
    }

    for template_path, target_path in templates.items():
        template_text = template_path.read_text()
        text = get_text(
            template_text,
            json,
            template_name=template_path.name)
        write_text_file(
            text,
            target_path,
            # checks for relevant changes between two texts to determine whether to skip writing into a file.
            diff_func=diff_text,
            # filters out lines when checking for differences.
            filter_func=lambda line, idx: idx < 5 and line.startswith("[//]: # (Auto-generated"),
            log_func=lambda message: print(message)
        )
