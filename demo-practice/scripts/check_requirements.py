import ast
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"

LOCAL_MODULES = {"app", "calc", "service"}
IGNORE_PACKAGES = {"pytest", "mypy", "ruff"}


def get_imports() -> set[str]:
    imports = set()

    for file_path in SRC_DIR.glob("*.py"):
        tree = ast.parse(file_path.read_text(encoding="utf-8"))

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])

    return {name for name in imports if name not in LOCAL_MODULES}


def get_requirements() -> set[str]:
    requirements = set()

    for line in REQUIREMENTS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            requirements.add(line.split("==")[0].strip().lower())

    return requirements


def main() -> int:
    imports = {name.lower() for name in get_imports()}
    requirements = get_requirements()

    missing = sorted(imports - requirements)
    extra = sorted(req for req in requirements - imports if req not in IGNORE_PACKAGES)

    if missing:
        print("Missing packages in requirements.txt:")
        for package in missing:
            print(f"  - {package}")

    if extra:
        print("Possibly unused packages in requirements.txt:")
        for package in extra:
            print(f"  - {package}")

    if missing:
        return 1

    print("Requirements check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
