---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

## Process
1. **Understand Intent**: What should the skill do? When should it trigger?
2. **Research**: Check existing tools, MCPs, and patterns.
3. **Draft SKILL.md**: Write clear instructions with name, description, and workflow.
4. **Test**: Create 2-3 test prompts and run Claude with access to the skill.
5. **Evaluate**: Help the user review results qualitatively and quantitatively.
6. **Iterate**: Improve the skill based on feedback.

## Skill Writing Tips
- **Name**: Clear and descriptive identifier.
- **Description**: This is the primary triggering mechanism. Include "when to use" info here. Make it a bit "pushy" to avoid undertriggering.
- **Imperative Form**: Use direct commands ("Do X", "Create Y").
- **Explain the Why**: LLMs work better when they understand the reasoning behind a constraint.
- **Progressive Disclosure**: Keep the main `SKILL.md` under 500 lines. Move large reference data or complex scripts to subdirectories.
- **Examples**: Include 1-2 input/output examples to anchor the behavior.

## Testing & Evaluation
- **Evals**: Save test cases in `evals/evals.json`.
- **Benchmarking**: Compare "with-skill" vs "without-skill" (or old vs new version).
- **Timing & Tokens**: Capture performance data from subagent notifications.
- **Human Review**: Use a viewer (like `generate_review.py`) to let the user see and grade outputs.

## Description Optimization
After a skill is functional, optimize the frontmatter description to ensure it triggers correctly. Generate 20 queries (10 should-trigger, 10 should-not-trigger) and run an optimization loop to find the best description.
