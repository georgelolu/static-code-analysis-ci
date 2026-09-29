# Static Code Analysis CI/CD

A practical DevSecOps project demonstrating how static code analysis and security scanning can be integrated into a GitHub Actions CI/CD pipeline.

The project evaluates and implements multiple static-analysis approaches for Python applications, including **Ruff, Semgrep, CodeQL, Black, Pylint, and Super-Linter**.

It also demonstrates an intentional code-quality failure, a security finding, remediation, and successful CI validation.

---

## 📌 Project Overview

Static code analysis examines source code without executing the application.

In a CI/CD environment, static analysis can automatically identify:

* Code-quality problems
* Formatting issues
* Maintainability problems
* Security vulnerabilities
* Dangerous coding patterns
* Type-checking problems
* Configuration errors

This project demonstrates how these checks can be integrated into GitHub Actions so that problems are detected automatically before code is merged.

---

## 🎯 Project Objectives

The main objectives are to:

1. Research static code analysis tools suitable for CI/CD.
2. Compare tools based on language support and capabilities.
3. Integrate multiple analysis tools into GitHub Actions.
4. Demonstrate intentional code-quality failures.
5. Demonstrate security findings using Semgrep.
6. Demonstrate deeper security analysis using CodeQL.
7. Demonstrate multi-linter validation using Super-Linter.
8. Document the CI/CD workflow and results.
9. Provide evidence of both failed and successful security checks.

---

# 🏗️ Architecture

```text
                         GitHub Repository
                                │
                                ▼
                       Push / Pull Request
                                │
                                ▼
                         GitHub Actions
                                │
              ┌─────────────────┼──────────────────┐
              │                 │                  │
              ▼                 ▼                  ▼
           pytest              Ruff             Semgrep
        Functional Tests   Python Linting       Security
              │                 │                  │
              └─────────────────┼──────────────────┘
                                │
                                ▼
                             CodeQL
                       Semantic Security
                           Analysis
                                │
                                ▼
                         Super-Linter
                    Multi-Linter Validation
                                │
                                ▼
                     Quality / Security Gate
                                │
                         ┌──────┴──────┐
                         │             │
                         ▼             ▼
                       FAIL          PASS
                         │             │
                     Fix Code        Merge
```

---

# 🛠️ Tools Evaluated

| Tool             | Primary Purpose                 | Language Focus | Security             | CI/CD Integration     |
| ---------------- | ------------------------------- | -------------- | -------------------- | --------------------- |
| **Ruff**         | Linting and code quality        | Python         | Limited              | Excellent             |
| **Semgrep**      | Pattern-based security analysis | Multi-language | Strong               | Excellent             |
| **CodeQL**       | Semantic security analysis      | Multi-language | Strong               | Excellent with GitHub |
| **Black**        | Code formatting                 | Python         | No                   | Excellent             |
| **Pylint**       | Code-quality analysis           | Python         | Limited              | Excellent             |
| **Super-Linter** | Multi-linter orchestration      | Multi-language | Depends on validator | Excellent             |

The tools serve different purposes and are therefore complementary rather than interchangeable.

---

# 🔍 Tool Details

## Ruff

Ruff is a fast Python linter and code-quality tool.

It was used to identify problems such as:

* Unused imports
* Python linting violations
* Code-quality issues

Example:

```bash
ruff check .
```

Successful result:

```text
All checks passed!
```

---

## Semgrep

Semgrep was used as the security-focused static analysis layer.

A custom rule was created to demonstrate detection of a hardcoded password:

```yaml
rules:
  - id: hardcoded-password
    languages:
      - python
    message: "Hard-coded password detected. Use environment variables or a secret manager."
    severity: ERROR
    patterns:
      - pattern: |
          return "SuperSecretPassword123"
```

The rule demonstrates how security-sensitive coding patterns can be detected automatically during CI.

Local scan:

```bash
semgrep scan --config=.semgrep/security.yml app/
```

---

## CodeQL

CodeQL provides deeper semantic analysis of source code.

It was integrated into GitHub Actions using the CodeQL Action for Python.

The workflow performs:

1. Repository checkout
2. CodeQL initialization
3. Python analysis
4. Security-result upload

CodeQL provides a different analysis approach from pattern-based tools such as Semgrep.

---

## Black

Black provides automated Python code formatting.

It was included through Super-Linter to ensure that Python source code follows consistent formatting rules.

Local validation:

```bash
black --check app/ tests/
```

Result:

```text
All done! ✨ 🍰 ✨
4 files would be left unchanged.
```

---

## Pylint

Pylint performs deeper Python code-quality analysis.

It checks areas such as:

* Documentation
* Naming conventions
* Code structure
* Potential programming errors
* Maintainability

The project initially failed Pylint because of missing documentation and naming issues.

After remediation:

```text
Your code has been rated at 10.00/10
```

---

## Super-Linter

Super-Linter was added as a multi-linter CI layer.

It validates the Python project using multiple tools, including:

* Ruff
* Black
* Flake8
* isort
* mypy
* Pylint

The workflow was deliberately kept separate from the Ruff, Semgrep, and CodeQL workflows so that each analysis layer could be demonstrated independently.

---

# 🚀 CI/CD Workflows

The project contains separate GitHub Actions workflows.

```text
.github/
└── workflows/
    ├── static-analysis.yml
    ├── semgrep.yml
    ├── codeql.yml
    └── super-linter.yml
```

### Static Analysis

Runs:

* pytest
* Ruff

### Semgrep

Runs security-focused pattern analysis.

### CodeQL

Runs semantic security analysis.

### Super-Linter

Runs multiple Python linters and formatters.

---

# 🧪 Testing

The project includes a basic unit test for the discount calculation.

Run locally:

```bash
python -m pytest -v
```

Expected result:

```text
1 passed
```

---

# 🔐 Security Demonstration

A major objective of this project was to demonstrate the complete security feedback loop.

## Step 1 — Introduce a security issue

A hardcoded password was intentionally placed in the application:

```python
def get_database_password():
    return "SuperSecretPassword123"
```

## Step 2 — Run Semgrep

```bash
semgrep scan --config=.semgrep/security.yml app/
```

The custom Semgrep rule detected the hardcoded credential pattern.

This demonstrated that the security gate could identify an intentionally introduced security issue.

## Step 3 — Capture evidence

The failed/security-finding state was captured as evidence.

## Step 4 — Remediate

The vulnerable demonstration code was subsequently remediated.

## Step 5 — Verify

The CI pipeline was rerun to verify that the security checks passed.

This demonstrates the DevSecOps feedback loop:

```text
Code Change
    ↓
Static Analysis
    ↓
Security Finding
    ↓
Developer Remediation
    ↓
Automated Verification
    ↓
Green Pipeline
```

---

# ❌ Code Quality Failure Demonstration

Ruff was also intentionally configured to detect an unused import.

Example:

```python
import os
```

The import was unused.

Ruff detected the issue:

```text
F401 `os` imported but unused
```

The issue was then removed.

After remediation:

```text
All checks passed!
```

Evidence was captured for the failed state.

---

# 📊 Final CI Results

| Check        | Result  |
| ------------ | ------- |
| pytest       | 🟢 PASS |
| Ruff         | 🟢 PASS |
| Black        | 🟢 PASS |
| Pylint       | 🟢 PASS |
| Semgrep      | 🟢 PASS |
| CodeQL       | 🟢 PASS |
| Super-Linter | 🟢 PASS |

The final project therefore demonstrates a fully functioning static-analysis CI/CD pipeline.

---

# 📸 Evidence

The project includes screenshots documenting important stages of the implementation.

### Ruff Failure

Ruff detected an intentionally unused import.

### Semgrep Security Check

Semgrep security validation successfully completed.

### CodeQL

CodeQL successfully completed its security analysis.

### Super-Linter

Super-Linter successfully completed the configured Python validation checks.

---

# 📁 Project Structure

```text
static-code-analysis-ci/
│
├── .github/
│   └── workflows/
│       ├── static-analysis.yml
│       ├── semgrep.yml
│       ├── codeql.yml
│       └── super-linter.yml
│
├── .semgrep/
│   └── security.yml
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── docs/
│   └── evidence/
│       ├── 03-ruff-failure.png
│       ├── 05-semgrep-security-green.png
│       ├── 06-codeql-security-green.png
│       └── 07-super-linter-green.png
│
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 💻 Local Setup

Clone the repository:

```bash
git clone https://github.com/georgelolu/static-code-analysis-ci.git
cd static-code-analysis-ci
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app/main.py
```

---

# 🧪 Run Tests

```bash
python -m pytest -v
```

---

# 🔎 Run Ruff

```bash
ruff check .
```

---

# 🎨 Run Black

```bash
black --check app/ tests/
```

---

# 📋 Run Pylint

```bash
pylint app tests
```

---

# 🔐 Run Semgrep

```bash
semgrep scan --config=.semgrep/security.yml app/
```

---

# 🔄 CI/CD Execution

The GitHub Actions workflows automatically execute when code is pushed to the `main` branch or when a pull request targets `main`.

Example workflow:

```text
Developer
    │
    ▼
Git Push / Pull Request
    │
    ▼
GitHub Actions
    │
    ├── pytest
    ├── Ruff
    ├── Semgrep
    ├── CodeQL
    └── Super-Linter
            │
            ▼
      Analysis Results
            │
       ┌────┴────┐
       ▼         ▼
     Failed    Passed
       │         │
       ▼         ▼
    Fix Code   Continue
                 │
                 ▼
              Merge
```

---

# 📈 Why Multiple Tools?

No single static-analysis tool performs every type of analysis equally.

This project therefore demonstrates a layered approach:

```text
Ruff
 │
 └── Fast Python linting

Black
 │
 └── Formatting consistency

Pylint
 │
 └── Python code quality

Semgrep
 │
 └── Security pattern detection

CodeQL
 │
 └── Semantic security analysis

Super-Linter
 │
 └── Multi-linter validation
```

This separation makes it possible to identify which tool is responsible for a particular class of problem.

---

# 🛡️ DevSecOps Approach

Security checks are integrated directly into the development workflow rather than being performed only after deployment.

```text
Plan
 ↓
Develop
 ↓
Commit
 ↓
CI Security Checks
 ↓
Static Analysis
 ↓
Test
 ↓
Remediate Findings
 ↓
Re-run Pipeline
 ↓
Merge
```

This approach helps provide earlier feedback to developers and reduces the chance that known code-quality or security issues progress unnoticed through the delivery pipeline.

---

# 📚 Key Lessons Learned

During implementation, the project demonstrated several practical CI/CD lessons:

* Static analysis is most useful when integrated directly into CI.
* Different tools detect different categories of issues.
* Security rules can be intentionally tested using controlled findings.
* Formatting and code-quality checks can cause CI failures even when application tests pass.
* CI environments may behave differently from local environments.
* Explicitly configuring validators makes multi-tool pipelines easier to control.
* Failed CI runs provide useful feedback for remediation.
* Security should be treated as part of the development lifecycle.

---

# 🔮 Future Improvements

Possible future enhancements include:

* Add dependency vulnerability scanning with `pip-audit`.
* Add container image scanning with Trivy.
* Add secret scanning.
* Add coverage reporting.
* Add branch protection requiring successful CI checks.
* Add pull-request security gates.
* Add SonarQube/SonarCloud for centralized quality reporting.
* Add automated security-report artifacts.
* Add deployment only after all required quality gates pass.

---

# 🏁 Conclusion

This project demonstrates how static code analysis can be integrated into a modern CI/CD pipeline using GitHub Actions.

The implementation combines:

* Automated testing
* Python linting
* Code formatting
* Code-quality analysis
* Security pattern detection
* Semantic security analysis
* Multi-linter validation

The project also demonstrates the complete remediation cycle:

```text
Introduce Issue
      ↓
Detect Issue
      ↓
CI Failure / Security Finding
      ↓
Remediate
      ↓
Re-run Analysis
      ↓
Green Pipeline
```

The result is a practical DevSecOps demonstration showing how automated analysis can be incorporated into the software delivery lifecycle.

---

## 👨‍💻 Author

**George Omololu Akinbi**

Cloud & DevOps Engineer

GitHub: https://github.com/Georgelolu

