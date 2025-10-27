# inventory
| Issue               | Type    | Line(s)        | Description                                            | Fix Approach                                      |
|---------------------|---------|----------------|--------------------------------------------------------|---------------------------------------------------|
| Mutable default arg | Bug     | 12             | logs=[] shared across calls                            | Change default to None and initialize in method    |
| Missing docstring   | Style   | All            | No documentation for module or functions               | Add informative docstrings                         |
| Naming not snake_case | Style | 8, 14, 22, 25, 31, 36, 41 | Function names use camelCase          | Rename functions to snake_case throughout          |
| Bare except         | Bug     | 19             | except: catches all exceptions and hides bugs          | Use except KeyError: and handle explicitly         |
| Insecure eval       | Security| 59             | eval() function can execute arbitrary code             | Remove eval() and use direct function call         |
| File handling       | Style   | 26, 32         | Files opened without context manager & encoding        | Use with open(..., encoding="utf-8") as f:         |
| Unused import       | Style   | 2              | import logging present but unused                      | Remove unused import statement                     |
| Missing blank lines | Style   | 8, 14, 22, ... | Less than 2 blank lines before/after funcs             | Add 2 blank lines between top-level functions      |
    


1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were style-related warnings, such as missing blank lines, unused imports, and changing function names from camelCase to snake_case. These only required small edits throughout the codebase and were clearly identified by the tools. The hardest issues involved changing or removing mutable default arguments and handling exceptions more precisely, because these fixes required a deeper understanding of how data flows through the code and attention to not introduce new bugs while restructuring function signatures or exception logic.

2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, occasionally the tools reported issues that were not genuinely problematic in context (false positives). For example, Pylint flagged the use of the global statement as a warning, even though it was needed for correct data loading in this small script. Similarly, style warnings about line lengths were sometimes raised for long strings that were still readable and necessary.

3. How would you integrate static analysis tools into your actual software development workflow?

In actual software development, I would run these static analysis tools both locally (before committing code) and as part of a Continuous Integration (CI) process. Setting up pre-commit hooks or automated CI jobs ensures that code meets quality standards before it's merged into the main branch. This practice helps catch issues early, enforces coding standards across the team, and prevents the introduction of security risks or maintainability problems.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the suggested fixes, the code became much more readable and organized: function names were consistent, documentation was present, and formatting was uniform. Robustness improved thanks to explicit exception handling and the elimination of potentially dangerous constructs like eval and mutable default arguments. Furthermore, the use of context managers and explicit UTF-8 encoding in file operations made the code safer and more portable