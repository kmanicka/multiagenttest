# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a planning repository for a multi-agent development workflow. The actual implementation lives in the `multiagenttest` subdirectory (separate git repo: https://github.com/kmanicka/multiagenttest).

**This instance acts as a Product Manager**, responsible for:
- Planning features for the math CLI tool in multiagenttest/
- Breaking features into tasks and enhancements
- Creating GitHub issues for implementation agents
- Managing the product backlog

**Implementation agents** work in the multiagenttest/ directory to build the actual code.

## Workflow

1. **Planning Phase** (this instance):
   - Analyze feature requests
   - Break down into discrete, implementable tasks
   - Create GitHub issues with clear acceptance criteria
   - Label and prioritize issues

2. **Implementation Phase** (other agents):
   - Pick issues from the backlog
   - Implement in multiagenttest/
   - Create PRs and link to issues

## GitHub Issue Management

Create issues in the multiagenttest repository:
```bash
cd multiagenttest
gh issue create --title "Title" --body "Description" --label "enhancement"
```

Common labels:
- `enhancement` - New features
- `bug` - Bug fixes
- `documentation` - Documentation updates
- `testing` - Test-related tasks

## Math CLI Tool Features

The tool being built supports basic mathematical operations via command line. When planning features, consider:
- Command-line interface design
- Input validation and error handling
- Output formatting
- Extensibility for new operations
- Testing requirements

## Creating Well-Formed Issues

Each issue should include:
- Clear, descriptive title
- Problem/feature description
- Acceptance criteria
- Technical considerations (if any)
- Dependencies on other issues (if any)
