# ${project_name}

[//]: # (badges)
[![Repo](https://img.shields.io/badge/repo-${repo_host}-${badge_color})](${repo_link})
[![Version](https://img.shields.io/badge/version-${version}-brightgreen.svg)](${repo_link}/releases)
[![PyPI](https://img.shields.io/pypi/v/${project_name})](${pypi_link}/#history)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/${project_name})
![PyPI - Status](https://img.shields.io/pypi/status/${project_name})
[![PyPI - License](https://img.shields.io/pypi/l/${project_name})](${license_file})
![PyPI - Format](https://img.shields.io/pypi/format/${project_name})
[![PyPI - Downloads](https://img.shields.io/pypi/dm/${project_name})](${pypi_link}/#files)

${description}

## Installation

```sh
pip install ${project_name}
```

## Usage

```python
from scriptgen import StringBuilder


if __name__ == "__main__":
    # Create a StringBuilder instance.
    sb = StringBuilder()

    sb.wt("Hello ")  # write text "Hello "
    sb.wl("World!")  # write line "World!\n"

    print(str(sb))
```

```
Hello World!

```

<hr/>

```python
from scriptgen import StringBuilder

from scriptgen.templates.csharp import \
    csharp_usings, \
    csharp_namespace, \
    csharp_class, \
    csharp_method


if __name__ == "__main__":
    # Create a StringBuilder instance.
    sb = StringBuilder()

    # Write using statements.
    sb.wb(csharp_usings(
        "System"
    ))

    # Add a new line after the using statements.
    sb.nl()

    # Create a namespace StringBuilder instance.
    ns = csharp_namespace("Sample")

    # Create a class StringBuilder instance.
    c = csharp_class(
        class_name="Program",
        access_modifier="public"
    )

    # Create a method StringBuilder instance.
    m = csharp_method(
        method_name="Main",
        access_modifier="public static",
        return_type="int"
    )

    # Write the following lines inside the method.
    m.wl('Console.WriteLine("Hello World!");')
    m.wl("return 0;")

    c.wb(m)  # Write the method inside the class.
    ns.wb(c)  # Write the class inside the namespace.
    sb.wb(ns)  # Write the namespace.

    print(str(sb))

```

```csharp
using System;

namespace Sample
{
    public class Program
    {
        public static int Main()
        {
            Console.WriteLine("Hello World!");
            return 0;
        }
    }
}

```

<hr/>

```python
from scriptgen import StringBuilder

from scriptgen.templates.csharp import \
    csharp_autogen, \
    csharp_namespace, \
    csharp_class, \
    csharp_region


if __name__ == "__main__":
    # Get version from arguments..
    # i.e. python script.py -major 0 -minor 0 -patch 1
    major: int = 0
    minor: int = 0
    patch: int = 1

    # Create a StringBuilder instance.
    sb = StringBuilder()

    # Write timestamp.
    sb.wb(csharp_autogen())

    # Add a new line after the using statements.
    sb.nl()

    # Create a namespace StringBuilder instance.
    ns = csharp_namespace("Sample")

    # Create a class StringBuilder instance.
    c = csharp_class(
        class_name="BuildInfo",
        access_modifier="public static partial"
    )

    # Create a "Constants" region StringBuilder instance.
    r = csharp_region("Constants")

    # Write the following lines inside the "Constants" region.
    r.wl(f"public const int MAJOR = {major};")
    r.nl()
    r.wl(f"public const int MINOR = {minor};")
    r.nl()
    r.wl(f"public const int PATCH = {patch};")

    c.wb(r)  # Write the region inside the class.
    ns.wb(c)  # Write the class inside the namespace.
    sb.wb(ns)  # Write the namespace.

    print(str(sb))

```

```csharp
// Auto-generated: 2020-03-15T04:20:47.909851

namespace Sample
{
    public static partial class BuildInfo
    {
        #region Constants
        
        public const int MAJOR = 0;
        
        public const int MINOR = 0;
        
        public const int PATCH = 1;
        
        #endregion Constants
    }
}

```

<hr/>

Look at this [script](tools/gen_docs.py) to see its practical use case.

## Contribution

Suggestions and contributions are always welcome.
Make sure to read the [Contribution Guidelines](${contributing_file}) file for more information before submitting a `${merge_term}`.

## License

`${project_name}` is released under the ${license_type} License. See the [LICENSE](${license_file}) file for details.