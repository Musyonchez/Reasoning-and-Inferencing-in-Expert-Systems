import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

with open("knowledge_base.json") as f:
    KB = json.load(f)

RULES = KB["rules"]


def get_student_facts(gpa, attendance, disciplinary, prerequisites, fees):
    facts = set()
    if gpa > 3.5:
        facts.add("gpa_above_3_5")
    elif 3.0 <= gpa <= 3.49:
        facts.add("gpa_between_3_and_3_49")
    else:
        facts.add("gpa_below_3")

    if attendance > 80:
        facts.add("attendance_above_80")
    else:
        facts.add("attendance_below_80")

    if disciplinary:
        facts.add("has_disciplinary_cases")
    else:
        facts.add("no_disciplinary_cases")

    if prerequisites:
        facts.add("completed_prerequisites")

    if fees:
        facts.add("has_outstanding_fees")
    else:
        facts.add("no_outstanding_fees")

    return facts


def forward_chain(facts):
    conclusions = []
    for rule in RULES:
        if all(c in facts for c in rule["conditions"]):
            conclusions.append(rule)
    return conclusions


def backward_chain(goal, facts):
    for rule in RULES:
        if rule["conclusion"] == goal:
            if all(c in facts for c in rule["conditions"]):
                return True, rule
    return False, None


def explain(conclusions):
    if not conclusions:
        print("  No conclusions reached.")
        return
    for rule in conclusions:
        print(f"  ✓ {rule['conclusion']}")
        print(f"    Because ({rule['name']}):")
        for c in rule["conditions"]:
            print(f"      - {KB['facts'][c]}")


def run_profile(name, gpa, attendance, disciplinary, prerequisites, fees):
    print(f"\n{'='*50}")
    print(f"Student: {name}")
    print(f"  GPA: {gpa} | Attendance: {attendance}% | Disciplinary: {disciplinary} | Prerequisites: {prerequisites} | Fees: {fees}")

    facts = get_student_facts(gpa, attendance, disciplinary, prerequisites, fees)

    print("\n[Forward Chaining]")
    conclusions = forward_chain(facts)
    explain(conclusions)

    print("\n[Backward Chaining - checking specific goals]")
    goals = ["Eligible for Scholarship", "Eligible for Graduation", "Academic Probation", "Registration Blocked", "Dean's List Candidate"]
    for goal in goals:
        met, rule = backward_chain(goal, facts)
        if met:
            print(f"  ✓ {goal} — verified via '{rule['name']}'")


if __name__ == "__main__":
    run_profile("Alice", gpa=3.8, attendance=90, disciplinary=False, prerequisites=True, fees=False)
    run_profile("Bob", gpa=3.1, attendance=75, disciplinary=False, prerequisites=True, fees=False)
    run_profile("Charlie", gpa=2.5, attendance=60, disciplinary=True, prerequisites=False, fees=True)
