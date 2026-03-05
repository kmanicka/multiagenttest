# Multi-Agent Development Planning Repository

This repository serves as the planning and orchestration hub for a multi-agent software development workflow. The actual implementation work happens in the [multiagenttest](https://github.com/kmanicka/multiagenttest) repository.

## Project Overview

**Project Goal:** Build a command-line tool for basic mathematical operations using a multi-agent development approach.

**Implementation Repository:** https://github.com/kmanicka/multiagenttest

## Multi-Agent Workflow

This project demonstrates a collaborative AI agent workflow with three distinct roles:

### 1. Planner Agent (This Repository)
- **Role:** Product Manager
- **Responsibilities:**
  - Analyze feature requests
  - Break down features into implementable tasks
  - Create GitHub issues with clear acceptance criteria
  - Manage the product backlog
  - Orchestrate work through GitHub Projects
- **Location:** Works in this repository (`planer/`)

### 2. Developer Agent (Implementation)
- **Role:** Software Engineer
- **Responsibilities:**
  - Clone the multiagenttest repository
  - Pick issues from the backlog (via GitHub Projects)
  - Implement features according to specifications
  - Write tests for implemented features
  - Create pull requests with detailed descriptions
  - Link PRs to issues
- **Location:** Works in `multiagenttest/` repository

### 3. Reviewer Agent (Code Review)
- **Role:** Code Reviewer / Tech Lead
- **Responsibilities:**
  - Review pull requests for code quality
  - Check test coverage and correctness
  - Verify adherence to acceptance criteria
  - Provide feedback or request changes
  - Merge approved PRs
  - Close associated issues
- **Location:** Works in `multiagenttest/` repository

## Project Status

### Current Phase: Planning Complete ✅

**Issues Created:** 7 issues in multiagenttest repository

| Issue # | Title | Type | Status |
|---------|-------|------|--------|
| #2 | Project Setup: Initialize Python CLI project structure | Foundation | OPEN |
| #3 | Feature: Implement basic addition operation | Feature | OPEN |
| #4 | Feature: Implement subtraction operation | Feature | OPEN |
| #5 | Feature: Implement multiplication operation | Feature | OPEN |
| #6 | Feature: Implement division operation | Feature | OPEN |
| #7 | Feature: Add unit tests for all operations | Testing | OPEN |
| #8 | Documentation: Create user guide and API documentation | Documentation | OPEN |

**Implementation Order:**
1. Phase 1: Issue #2 (Project Setup) - **Must be done first**
2. Phase 2: Issues #3-6 (Core Operations) - Can be parallelized
3. Phase 3: Issue #7 (Testing)
4. Phase 4: Issue #8 (Documentation)

---

## Instructions for Developer Agent

### Initial Setup

1. **Clone the implementation repository:**
   ```bash
   git clone https://github.com/kmanicka/multiagenttest.git
   cd multiagenttest
   ```

2. **Check available issues:**
   ```bash
   gh issue list --state open
   ```

3. **Identify your task from GitHub Project board** (preferred) or pick the next available issue following the implementation order.

### Development Workflow

#### Step 1: Pick an Issue
```bash
# View issue details
gh issue view <issue-number>

# Self-assign the issue
gh issue edit <issue-number> --add-assignee @me
```

#### Step 2: Create a Feature Branch
```bash
# Create and switch to a new branch
git checkout -b feature/issue-<issue-number>-<short-description>

# Example:
git checkout -b feature/issue-2-project-setup
```

#### Step 3: Implement the Feature
- Read the issue's acceptance criteria carefully
- Implement all requirements listed
- Follow Python best practices
- Write clean, maintainable code
- Add appropriate error handling
- Include docstrings for functions

#### Step 4: Test Your Implementation
```bash
# Run tests locally
pytest

# Check code coverage (if applicable)
pytest --cov
```

#### Step 5: Commit Your Changes
```bash
# Stage your changes
git add <files>

# Commit with a descriptive message
git commit -m "Implement <feature>: <brief description>

- Acceptance criterion 1
- Acceptance criterion 2
- Additional details if needed

Closes #<issue-number>"
```

#### Step 6: Push and Create Pull Request
```bash
# Push your branch
git push -u origin feature/issue-<issue-number>-<short-description>

# Create PR with gh CLI
gh pr create --title "Implement <feature>" --body "$(cat <<'EOF'
## Summary
Brief description of what was implemented.

## Changes
- List of key changes
- Technical decisions made
- Any deviations from the original issue (with justification)

## Testing
- Description of tests added
- How to verify the implementation

## Checklist
- [ ] All acceptance criteria met
- [ ] Tests written and passing
- [ ] Code follows project conventions
- [ ] Documentation updated (if needed)

Closes #<issue-number>
EOF
)"
```

### Best Practices for Developer Agent

1. **One Issue at a Time:** Complete one issue fully before starting another
2. **Follow Dependencies:** Ensure prerequisite issues are completed first (check issue dependencies)
3. **Match Acceptance Criteria:** Every checkbox in the issue should be addressed
4. **Write Tests:** Include tests for your implementation when applicable
5. **Clear Commit Messages:** Use conventional commit format
6. **Link Issues:** Always reference the issue number in your PR
7. **Keep PRs Focused:** One PR per issue, no scope creep
8. **Self-Review:** Review your own code before creating the PR

---

## Instructions for Reviewer Agent

### Review Workflow

#### Step 1: Check for New Pull Requests
```bash
# List open pull requests
gh pr list --state open

# View a specific PR
gh pr view <pr-number>
```

#### Step 2: Checkout and Review the PR
```bash
# Checkout the PR branch
gh pr checkout <pr-number>

# Review the code changes
gh pr diff <pr-number>
```

#### Step 3: Run Tests and Validation
```bash
# Install dependencies (if needed)
pip install -e .

# Run all tests
pytest

# Check code coverage
pytest --cov

# Try the implemented feature manually
# Example: python -m mathcli add 5 10
```

#### Step 4: Review Against Acceptance Criteria
- Open the linked issue: `gh issue view <issue-number>`
- Verify each acceptance criterion is met
- Check code quality:
  - Follows Python best practices (PEP 8)
  - Proper error handling
  - Clear variable/function names
  - Adequate documentation
  - No security vulnerabilities
  - No unnecessary complexity

#### Step 5: Provide Feedback or Approve

**If Changes Needed:**
```bash
gh pr review <pr-number> --request-changes --body "$(cat <<'EOF'
## Changes Requested

### Issue 1: [Brief description]
**Location:** `file.py:line_number`
**Problem:** [Describe the issue]
**Suggestion:** [How to fix it]

### Issue 2: [Brief description]
...

## Summary
Please address these items and update the PR.
EOF
)"
```

**If Approved:**
```bash
gh pr review <pr-number> --approve --body "$(cat <<'EOF'
## Review Summary
✅ All acceptance criteria met
✅ Tests passing
✅ Code quality excellent
✅ No issues found

Great work! This implementation is ready to merge.
EOF
)"
```

#### Step 6: Merge the PR
```bash
# Merge using squash (recommended for clean history)
gh pr merge <pr-number> --squash --delete-branch

# Or merge with merge commit
gh pr merge <pr-number> --merge --delete-branch

# Or rebase merge
gh pr merge <pr-number> --rebase --delete-branch
```

The associated issue will automatically close if the PR description contains "Closes #issue-number".

### Best Practices for Reviewer Agent

1. **Timely Reviews:** Review PRs promptly to unblock development
2. **Thorough Testing:** Always run tests and try the feature manually
3. **Constructive Feedback:** Be specific and helpful in review comments
4. **Check Issue Alignment:** Verify the PR actually solves the issue
5. **Security First:** Watch for security issues (injection, validation, etc.)
6. **Maintain Standards:** Ensure consistency across the codebase
7. **Document Decisions:** If accepting a deviation from the spec, document why

---

## GitHub Project Orchestration

**Project Board:** Used to track issue status and workflow

### Recommended Project Columns:
1. **Backlog** - New issues awaiting prioritization
2. **Ready** - Issues ready to be picked up (no blockers)
3. **In Progress** - Issues currently being worked on
4. **In Review** - PRs awaiting review
5. **Done** - Completed and merged

### Using the Project Board

**Developer Agent:**
- Move issues to "In Progress" when starting work
- Move to "In Review" when PR is created

**Reviewer Agent:**
- Pick PRs from "In Review"
- Move to "Done" after merging

**Planner Agent:**
- Create new issues in "Backlog"
- Move issues to "Ready" when properly specified

---

## Repository Structure

```
planer/                          # This repository (planning)
├── CLAUDE.md                    # Guidance for Claude Code instances
├── README.md                    # This file
├── PLANNING_SESSION.md          # Planning session notes
└── multiagenttest/              # Submodule/reference to implementation repo

multiagenttest/                  # Implementation repository
├── src/                         # Source code
│   └── mathcli/                 # CLI package
├── tests/                       # Test files
├── setup.py / pyproject.toml    # Package configuration
├── requirements.txt             # Dependencies
├── README.md                    # User documentation
└── .github/                     # GitHub workflows (CI/CD)
```

---

## Communication Between Agents

### Issue Comments
Use issue comments for clarifications or status updates:
```bash
gh issue comment <issue-number> --body "Status update or question"
```

### PR Reviews
Use PR review comments for code-specific feedback:
```bash
gh pr review <pr-number> --comment --body "General comment"
```

### Mentions
Tag specific agents or maintainers when needed:
```
@kmanicka - for project owner questions
```

---

## Quick Reference Commands

### Developer Agent Commands
```bash
# Issue management
gh issue list
gh issue view <number>
gh issue edit <number> --add-assignee @me

# Branch management
git checkout -b feature/issue-<number>-description
git add .
git commit -m "message"
git push -u origin branch-name

# PR creation
gh pr create --title "Title" --body "Description"
gh pr list
```

### Reviewer Agent Commands
```bash
# PR management
gh pr list
gh pr view <number>
gh pr checkout <number>
gh pr diff <number>

# Review actions
gh pr review <number> --approve
gh pr review <number> --request-changes
gh pr merge <number> --squash --delete-branch
```

### Planner Agent Commands
```bash
# Issue creation
gh issue create --title "Title" --body "Description" --label "enhancement"

# Project management
gh issue list --state open
gh issue edit <number> --add-label "label"
```

---

## Getting Help

- **Repository Issues:** https://github.com/kmanicka/multiagenttest/issues
- **Project Owner:** @kmanicka
- **Planning Repository:** https://github.com/kmanicka/planer

---

## License

[Specify license if applicable]

## Contributing

This is a multi-agent demonstration project. For questions or suggestions, please open an issue in the appropriate repository.
