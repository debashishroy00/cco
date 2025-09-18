#!/usr/bin/env python3
"""CCOM CLI - Claude Code Orchestrator and Memory"""

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

    print("Initializing CCOM v0.2...")

    # Create .claude directory
    claude_dir = current_dir / ".claude"
    claude_dir.mkdir(exist_ok=True)

    # Create archive directory
    archive_dir = claude_dir / "archive"
    archive_dir.mkdir(exist_ok=True)

    # Copy CLAUDE.md
    claude_md_src = template_dir / "CLAUDE.md"
    claude_md_dst = current_dir / "CLAUDE.md"

    if claude_md_dst.exists():
        print(f"WARNING: CLAUDE.md already exists, backing up to CLAUDE.md.bak")
        shutil.copy2(claude_md_dst, current_dir / "CLAUDE.md.bak")

    shutil.copy2(claude_md_src, claude_md_dst)
    print(f"Created CLAUDE.md")

    # Copy ccom.js
    ccom_js_src = template_dir / "ccom.js"
    ccom_js_dst = claude_dir / "ccom.js"
    shutil.copy2(ccom_js_src, ccom_js_dst)
    print(f"Created .claude/ccom.js")
    print(f"Created .claude/archive/")

    print("\nCCOM v0.2 initialized!")
    print("\nTest it:")
    print("  ccom status")
    print("  ccom remember 'my feature'")
    print("  ccom memory")
    print("\nMemory management:")
    print("  ccom stats")
    print("  ccom list")
    print("  ccom archive 30")

    return True

def show_status():
    """Show CCO status in current directory"""
    claude_dir = Path.cwd() / ".claude"
    memory_file = claude_dir / "memory.json"

    if not claude_dir.exists():
        print("ERROR: CCOM not initialized. Run 'ccom init' first.")
        return False

    if not memory_file.exists():
        print("CCOM initialized but no memory yet.")
        return True

    # Run the node command to show status
    os.system("node .claude/ccom.js start")
    return True

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="CCOM - Claude Code Orchestrator and Memory",
        epilog="For more info: https://github.com/debashishroy00/ccom"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize CCOM in current directory")

    # Status command
    status_parser = subparsers.add_parser("status", help="Show CCOM status")

    # Memory command
    memory_parser = subparsers.add_parser("memory", help="Show memory contents")

    # Remember command
    remember_parser = subparsers.add_parser("remember", help="Remember a feature")
    remember_parser.add_argument("name", help="Feature name to remember")

    # Clear command
    clear_parser = subparsers.add_parser("clear", help="Clear memory")

    # v0.2 Memory Management Commands
    stats_parser = subparsers.add_parser("stats", help="Show memory usage statistics")

    list_parser = subparsers.add_parser("list", help="List features with age")
    list_parser.add_argument("sort", nargs="?", default="created", help="Sort by: created or name")

    archive_parser = subparsers.add_parser("archive", help="Archive old features")
    archive_parser.add_argument("days", nargs="?", type=int, default=30, help="Archive features older than N days (default: 30)")

    remove_parser = subparsers.add_parser("remove", help="Remove specific feature")
    remove_parser.add_argument("name", help="Feature name to remove")

    compact_parser = subparsers.add_parser("compact", help="Compact memory by truncating long descriptions")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "init":
        init_project()
    elif args.command == "status":
        show_status()
    elif args.command == "memory":
        os.system("node .claude/ccom.js memory")
    elif args.command == "remember":
        os.system(f'node .claude/ccom.js remember "{args.name}"')
    elif args.command == "clear":
        os.system("node .claude/ccom.js clear")
    elif args.command == "stats":
        os.system("node .claude/ccom.js stats")
    elif args.command == "list":
        os.system(f"node .claude/ccom.js list {args.sort}")
    elif args.command == "archive":
        os.system(f"node .claude/ccom.js archive {args.days}")
    elif args.command == "remove":
        os.system(f'node .claude/ccom.js remove "{args.name}"')
    elif args.command == "compact":
        os.system("node .claude/ccom.js compact")

if __name__ == "__main__":
    main()