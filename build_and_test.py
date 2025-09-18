#!/usr/bin/env python3
"""Build and test the pip package"""

import subprocess
import sys
import tempfile
import os
from pathlib import Path

def run_command(cmd, check=True):
    """Run a command and return result"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"ERROR: Command failed: {cmd}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        return False
    return result

def build_package():
    """Build the package"""
    print("Building package...")

    # Clean old builds
    run_command("rm -rf build dist *.egg-info", check=False)

    # Build
    result = run_command("python -m build")
    if not result:
        return False

    print("Package built successfully!")
    return True

def test_install():
    """Test pip install in virtual environment"""
    print("Testing pip install...")

    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Creating test environment in {temp_dir}")

        # Create virtual environment
        venv_dir = Path(temp_dir) / "test_env"
        result = run_command(f"python -m venv {venv_dir}")
        if not result:
            return False

        # Get pip path
        if sys.platform == "win32":
            pip_path = venv_dir / "Scripts" / "pip.exe"
        else:
            pip_path = venv_dir / "bin" / "pip"

        # Install our package
        dist_file = list(Path("dist").glob("*.whl"))[0]
        result = run_command(f"{pip_path} install {dist_file}")
        if not result:
            return False

        # Test the CLI
        if sys.platform == "win32":
            cco_path = venv_dir / "Scripts" / "cco.exe"
        else:
            cco_path = venv_dir / "bin" / "cco"

        # Create test project
        test_project = Path(temp_dir) / "test_project"
        test_project.mkdir()
        os.chdir(test_project)

        # Test init
        result = run_command(f"{cco_path} init")
        if not result:
            return False

        # Verify files exist
        if not (test_project / "CLAUDE.md").exists():
            print("ERROR: CLAUDE.md not created")
            return False

        if not (test_project / ".claude" / "cco.js").exists():
            print("ERROR: .claude/cco.js not created")
            return False

        print("SUCCESS: pip install cco works!")
        return True

def main():
    """Main test function"""
    print("CCO Package Build and Test")
    print("=" * 40)

    # Build package
    if not build_package():
        print("Build failed!")
        return False

    # Test install
    if not test_install():
        print("Install test failed!")
        return False

    print("\n" + "=" * 40)
    print("🎉 SUCCESS! Ready for PyPI:")
    print("1. pip install cco")
    print("2. cco init")
    print("3. Memory works!")

    return True

if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)