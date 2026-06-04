# APT 3020 – Lab 2: Reasoning and Inferencing in Expert Systems

## Introduction
A rule-based expert system that advises students on academic outcomes using forward and backward chaining inference.

## Problem Statement
A university advisor system that takes student attributes (GPA, attendance, disciplinary record, prerequisites, fees) and applies rules to generate conclusions like scholarship eligibility, graduation status, or academic probation.

## Knowledge Base
Defined in `knowledge_base.json`. Facts represent student attributes; rules define conditions and conclusions.

## Rules Implemented
| Rule | Conditions | Conclusion |
|------|-----------|------------|
| Scholarship | GPA > 3.5, Attendance > 80%, No disciplinary cases | Eligible for Scholarship |
| Graduation | GPA ≥ 3.0, Prerequisites done, No fees | Eligible for Graduation |
| Probation | GPA < 3.0 | Academic Probation |
| Registration Block | Has outstanding fees | Registration Blocked |
| Dean's List | GPA > 3.5, Attendance > 80% | Dean's List Candidate |

## Reasoning Method
- **Forward Chaining**: Starts from known facts, fires all matching rules, collects conclusions.
- **Backward Chaining** (Bonus): Starts from a goal, checks if the required conditions are satisfied in the current facts.

## How to Run

```bash
python reasoning_engine.py
```

Requires Python 3.x. No external dependencies.

## Sample Output

```
Student: Alice | GPA: 3.8 | Attendance: 90% | ...

[Forward Chaining]
  ✓ Eligible for Scholarship
    Because (Scholarship Rule):
      - GPA Above 3.5
      - Attendance Above 80%
      - No Disciplinary Cases
  ✓ Eligible for Graduation
  ✓ Dean's List Candidate

[Backward Chaining]
  ✓ Eligible for Scholarship — verified via 'Scholarship Rule'
  ✓ Eligible for Graduation — verified via 'Graduation Rule'
  ✓ Dean's List Candidate — verified via 'Dean's List Rule'
```

## Repository Structure
```
├── README.md
├── reasoning_engine.py
├── knowledge_base.json
├── diagrams/
│   └── inference_flow.png
├── screenshots/
│   ├── test_case1.png
│   ├── test_case2.png
│   └── test_case3.png
└── docs/
    └── explanation_report.pdf
```
