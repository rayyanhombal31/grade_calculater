# grade_calculator.py

def average(marks):
    """Return the arithmetic average of a non-empty list of marks (0-100)."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")
    for m in marks:
        if m < 0 or m > 100:
            raise ValueError(f"Invalid mark: {m}. Marks must be between 0 and 100.")
    return round(sum(marks) / len(marks), 2)


def grade(avg):
    """Return letter grade based on average score (0-100)."""
    if avg < 0 or avg > 100:
        raise ValueError(f"Invalid average: {avg}. Must be between 0 and 100.")
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def is_pass(marks):
    """Return True if every subject mark >= 40 and overall average >= 50."""
    avg = average(marks)
    return all(m >= 40 for m in marks) and avg >= 50


if __name__ == "__main__":
    sample_1 = [88, 92, 79, 85, 91]
    sample_2 = [75, 80, 35, 70, 68]
    print("Sample 1 Marks:", sample_1)
    print("average(sample_1):", average(sample_1))
    print("grade(average(sample_1)):", grade(average(sample_1)))
    print("is_pass(sample_1):", is_pass(sample_1))
    print("-" * 40)
    print("Sample 2 Marks:", sample_2)
    print("average(sample_2):", average(sample_2))
    print("grade(average(sample_2)):", grade(average(sample_2)))
    print("is_pass(sample_2):", is_pass(sample_2))
