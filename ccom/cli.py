#!/usr/bin/env python3
"""
Enhanced CCOM CLI v0.3 - Vibe Coder Interface
Advanced natural language processing and enterprise automation
"""

import sys
import argparse
from pathlib import Path
from orchestrator import CCOMOrchestrator

def create_enhanced_cli():
    """Create enhanced CLI with natural language support"""
    parser = argparse.ArgumentParser(
        description="CCOM v0.3 - Claude Code Orchestrator and Memory",
        epilog="Natural language examples: 'deploy my app', 'check security', 'quality audit'",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Add natural language support
    parser.add_argument('command', nargs='*',
                       help='Natural language command or traditional command')

    # Traditional commands
    parser.add_argument('--status', action='store_true',
                       help='Show CCOM and project status')
    parser.add_argument('--memory', action='store_true',
                       help='Show memory contents')
    parser.add_argument('--stats', action='store_true',
                       help='Show memory statistics')
    parser.add_argument('--remember', type=str,
                       help='Remember a feature: --remember "auth system"')
    parser.add_argument('--init', action='store_true',
                       help='Initialize CCOM in current directory')

    # Advanced options
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output for debugging')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without executing')

    return parser

def handle_traditional_commands(args, orchestrator):
    """Handle traditional flag-based commands"""
    if args.status:
        orchestrator.show_status()
        return True
    elif args.memory:
        orchestrator.show_memory()
        return True
    elif args.remember:
        orchestrator.handle_memory_command(f"remember {args.remember}")
        return True
    elif args.init:
        init_ccom_project()
        return True

    return False

def init_ccom_project():
    """Initialize CCOM in current project"""
    print("🚀 Initializing CCOM v0.3 in current project...")

    current_dir = Path.cwd()
    claude_dir = current_dir / ".claude"

    # Create directories
    claude_dir.mkdir(exist_ok=True)
    agents_dir = claude_dir / "agents"
    agents_dir.mkdir(exist_ok=True)

    # Copy agents from CCOM installation
    ccom_dir = Path(__file__).parent.parent
    source_agents = ccom_dir / ".claude" / "agents"

    if source_agents.exists():
        import shutil
        for agent_file in source_agents.glob("*.md"):
            dest_file = agents_dir / agent_file.name
            shutil.copy2(agent_file, dest_file)
            print(f"✅ Installed agent: {agent_file.name}")

    # Create enhanced CLAUDE.md
    claude_md = current_dir / "CLAUDE.md"
    if not claude_md.exists():
        create_enhanced_claude_md(claude_md)
        print("✅ Created enhanced CLAUDE.md")

    # Initialize memory
    orchestrator = CCOMOrchestrator()
    orchestrator.save_memory()
    print("✅ Initialized memory system")

    print("\n🎉 CCOM v0.3 initialized successfully!")
    print("\n📖 Try these commands:")
    print("  ccom 'deploy my app'")
    print("  ccom 'check security'")
    print("  ccom 'quality audit'")
    print("  ccom --status")

def create_enhanced_claude_md(claude_md_path):
    """Create enhanced CLAUDE.md with CCOM configuration"""
    content = """# CCOM Enterprise Configuration v0.3

## Project Overview
This project uses CCOM v0.3 for enterprise-grade development with vibe coder confidence.

## Quality Standards
- **ESLint**: Essential production rules automatically enforced
- **Prettier**: Consistent formatting across all files
- **Security**: Comprehensive vulnerability scanning
- **Git Hooks**: Quality checks run automatically on commit

## Available CCOM Commands

### Natural Language (Recommended)
- `ccom "deploy my app"` - Full enterprise deployment with all gates
- `ccom "check security"` - Comprehensive security audit
- `ccom "quality audit"` - Code quality analysis and fixes
- `ccom "status"` - Show enterprise readiness dashboard

### Traditional Commands
- `ccom --status` - Project status
- `ccom --memory` - Show remembered features
- `ccom --remember "feature name"` - Add feature to memory

## For Claude Code
When generating code:
- Always include proper error handling
- Follow ESLint rules in .eslintrc.js
- Use TypeScript when available
- Format according to .prettierrc
- Consider security implications

## Enterprise Features
- **Quality Gates**: Automatic code quality enforcement
- **Security Scanning**: Vulnerability detection and hardening
- **Deployment Pipeline**: Safe, monitored production deployments
- **Memory System**: Cross-session feature tracking
- **Git Integration**: Pre-commit quality checks

## Subagents Available
- **quality-enforcer**: Ensures enterprise code standards
- **security-guardian**: Comprehensive security scanning and hardening
- **deployment-specialist**: Coordinates safe production deployments

## For Vibe Coders
Focus on building features. CCOM handles all the complex quality/security/deployment details automatically.
Your apps will be enterprise-grade without the enterprise complexity.
"""

    with open(claude_md_path, 'w') as f:
        f.write(content)

def show_help():
    """Show enhanced help with examples"""
    print("""
🚀 CCOM v0.3 - Claude Code Orchestrator and Memory

NATURAL LANGUAGE COMMANDS (Recommended):
  ccom "deploy my app"              → Enterprise deployment pipeline
  ccom "check security"             → Comprehensive security audit
  ccom "quality audit"              → Code quality analysis
  ccom "make it secure"             → Security hardening
  ccom "ship it to production"      → Full deployment sequence

TRADITIONAL COMMANDS:
  ccom --status                     → Show project status
  ccom --memory                     → Show remembered features
  ccom --remember "feature name"    → Add feature to memory
  ccom --init                       → Initialize CCOM in project

EXAMPLES:
  ccom "deploy"                     → Quick deployment
  ccom "security scan"              → Security check
  ccom "fix quality issues"         → Auto-fix code quality
  ccom --status                     → Traditional status check

ENTERPRISE FEATURES:
  ✅ Multi-agent orchestration (quality, security, deployment)
  ✅ Git hooks integration (automatic quality gates)
  ✅ Memory system (cross-session feature tracking)
  ✅ Natural language processing (vibe coder friendly)
  ✅ Enterprise security scanning (vulnerability detection)
  ✅ Production deployment pipeline (zero-downtime)

For more info: https://github.com/your-repo/ccom
""")

def main():
    """Enhanced main CLI entry point"""
    parser = create_enhanced_cli()

    # Handle no arguments
    if len(sys.argv) == 1:
        show_help()
        return

    args = parser.parse_args()

    try:
        orchestrator = CCOMOrchestrator()

        # Handle traditional commands first
        if handle_traditional_commands(args, orchestrator):
            return

        # Handle natural language commands
        if args.command:
            command_text = " ".join(args.command)

            if args.verbose:
                print(f"🔍 Processing: '{command_text}'")

            if args.dry_run:
                print(f"🧪 Dry run: Would execute '{command_text}'")
                return

            orchestrator.handle_natural_language(command_text)
        else:
            print("❓ No command provided. Use 'ccom --help' for usage.")

    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()