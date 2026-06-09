#!/usr/bin/env python3
"""Run all linting scripts in sequence and produce a combined health report."""

import subprocess
import sys
from pathlib import Path

def run_script(script_path):
    print(f"\n{'='*60}")
    print(f"Running {script_path.name}...")
    print('='*60)
    # Use the same Python interpreter that invoked this script (respects venv)
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

if __name__ == "__main__":
    scripts_dir = Path(__file__).parent
    run_script(scripts_dir / "validate_schema.py")
    run_script(scripts_dir / "check_wikilinks.py")
    run_script(scripts_dir / "review_queue.py")
    print("\nAll linting complete. Check wiki/09-indexes/ for reports.")
