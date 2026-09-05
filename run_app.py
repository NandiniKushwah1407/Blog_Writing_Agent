from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def python_executable() -> str:
    if os.name == "nt":
        venv_python = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
    else:
        venv_python = PROJECT_ROOT / ".venv" / "bin" / "python"

    return str(venv_python) if venv_python.exists() else sys.executable


def main() -> int:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(PROJECT_ROOT)

    command = [
        python_executable(),
        "-m",
        "streamlit",
        "run",
        "frontend/app.py",
    ]

    try:
        return subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            env=environment,
            check=False,
        ).returncode
    except FileNotFoundError:
        print("Python was not found. Install Python 3.11 or newer.")
        return 1
    except KeyboardInterrupt:
        print("\nBlogForge stopped.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
