#!/usr/bin/env python3
"""CCO CLI - One command installation"""

import os
import sys
import shutil
import argparse
from pathlib import Path

def get_template_path():
    """Get path to template files"""
    return Path(__file__).parent / "templates"

def init_project():
    """Initialize CCO in current directory"""
    current_dir = Path.cwd()
    template_dir = get_template_path()

    print("Initializing CCO v0.1...")

    # Create .claude directory
    claude_dir = current_dir / ".claude"
    claude_dir.mkdir(exist_ok=True)

    # Copy CLAUDE.md
    claude_md_src = template_dir / "CLAUDE.md"
    claude_md_dst = current_dir / "CLAUDE.md"

    if claude_md_dst.exists():
        print(f"WARNING: CLAUDE.md already exists, backing up to CLAUDE.md.bak")
        shutil.copy2(claude_md_dst, current_dir / "CLAUDE.md.bak")

    shutil.copy2(claude_md_src, claude_md_dst)
    print(f"Created CLAUDE.md")

    # Copy cco.js
    cco_js_src = template_dir / "cco.js"
    cco_js_dst = claude_dir / "cco.js"
    shutil.copy2(cco_js_src, cco_js_dst)
    print(f"Created .claude/cco.js")

    print("\nCCO initialized!")
    print("\nTest it:")
    print("  node .claude/cco.js start")
    print("  node .claude/cco.js remember 'my feature'")
    print("  node .claude/cco.js memory")

    return True

def show_status():
    """Show CCO status in current directory"""
    claude_dir = Path.cwd() / ".claude"
    memory_file = claude_dir / "memory.json"

    if not claude_dir.exists():
        print("ERROR: CCO not initialized. Run 'cco init' first.")
        return False

    if not memory_file.exists():
        print("CCO initialized but no memory yet.")
        return True

    # Run the node command to show status
    os.system("node .claude/cco.js start")
    return True

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="CCO - Claude Code Orchestrator",
        epilog="For more info: https://github.com/debashishroy00/cco"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize CCO in current directory")

    # Status command
    status_parser = subparsers.add_parser("status", help="Show CCO status")

    # Memory command
    memory_parser = subparsers.add_parser("memory", help="Show memory contents")

    # Remember command
    remember_parser = subparsers.add_parser("remember", help="Remember a feature")
    remember_parser.add_argument("name", help="Feature name to remember")

    # Clear command
    clear_parser = subparsers.add_parser("clear", help="Clear memory")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "init":
        init_project()
    elif args.command == "status":
        show_status()
    elif args.command == "memory":
        os.system("node .claude/cco.js memory")
    elif args.command == "remember":
        os.system(f'node .claude/cco.js remember "{args.name}"')
    elif args.command == "clear":
        os.system("node .claude/cco.js clear")

if __name__ == "__main__":
    main()