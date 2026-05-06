# Repository Routing Instructions

Use the `algorithm-problem-solver` skill whenever the user asks to solve, explain, or generate files for an algorithm or coding interview problem.

## When to use the skill

Use the skill if the user:
- pastes a LeetCode / algorithm / data structures problem
- asks for brute-force and optimal solutions
- asks for Python and JavaScript implementations
- asks for tests
- asks for a Markdown explanation file
- asks for multiple files per problem

## Expected output structure

For each problem, generate files under:

algorithms/
  <problem_slug>/
    <problem_slug>.md
    <problem_slug>.py
    <problem_slug>.js

Use kebab-case for `<problem_slug>`.

## Behavior rules

- Always follow the skill for algorithm problems
- Prefer creating all 3 files
- Keep explanations clear and interview-oriented
- Include both brute-force and optimal solutions unless they are effectively identical
- Include runnable tests in Python and JavaScript
- If the problem is ambiguous, state assumptions clearly
