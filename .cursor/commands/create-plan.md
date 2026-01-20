# /create-plan

Based on our exploration exchange, create a detailed implementation plan.

## Output Format
Create a markdown file in the project with this structure:

```markdown
# Plan: [Feature Name]

## TLDR
[1-2 sentence summary of what we're building]

## Critical Decisions
- [Decision 1]: [Rationale]
- [Decision 2]: [Rationale]

## Tasks

### 1. [Task Name]
- **Status**: [ ] Not Started
- **Description**: [What needs to be done]
- **Files**: [Files to be modified/created]

### 2. [Task Name]
- **Status**: [ ] Not Started
- **Description**: [What needs to be done]
- **Files**: [Files to be modified/created]

[Continue for all tasks...]
```

## Guidelines
- Keep steps clear, minimal, and concise
- Each task should be independently executable
- Update status as you work through the plan: [ ] Not Started, [~] In Progress, [x] Complete
- Consider splitting frontend/backend if using different models
- This plan will be referenced by other agents, so be explicit
