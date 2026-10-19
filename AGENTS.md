# Critical Rules
* Use `uv` to run all project specific development commands.
* Run `uv run nox` and ensure all checks pass before completing any task.
* Ensure you comply with all project linting and testing rules. I.e. Add no suppressions.
* Write tests from public APIs and write no tautological tests.
* Tests should only tests real use-cases and functional requirements. 