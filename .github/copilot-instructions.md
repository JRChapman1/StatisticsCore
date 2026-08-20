## Project purpose

This project is primarily intended to develop understanding of mathematics,
statistics, finance, actuarial modelling, and insurance.

The user normally writes the mathematical derivation, reference implementation,
and mathematical tests before asking Copilot for assistance.

When reviewing this work:
- Prioritise identifying mathematical, statistical, or conceptual errors.
- Do not replace the user's implementation merely because a more elegant implementation exists.
- Distinguish model/methodology issues from software-engineering issues.

When asked to productionise code:
- Preserve the model methodology and behaviour.
- Improve software engineering separately: structure, typing, validation,
  robustness, performance, documentation, and engineering test coverage.
- Do not silently change algorithms, approximations, parameterisations,
  numerical methods, conventions, assumptions, or modelling methodology.
- Treat any such change as a substantive model change requiring explicit user review.