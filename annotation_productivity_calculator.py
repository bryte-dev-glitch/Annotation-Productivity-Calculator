# Annotation Productivity Calculator
print("======================================")
print("    ANNOTATION PRODUCTIVITY CALCULATOR")
print("======================================")

# Constants
SHIFT_HOURS = 8
SECONDS_PER_HOUR = 3600
DAILY_TARGET = 11500
EXCELLENT_THRESHOLD = 1500
GOOD_THRESHOLD = 1250
AVERAGE_THRESHOLD = 1000
QUALITY_THRESHOLD = 98

# Get user input
name = input("Enter your name: ")
labels = int(input("Enter your labels: "))
hours_worked = float(input("Enter hours you've worked: "))
accuracy = float(input("Enter your accuracy (%): "))

# Check for invalid input
if hours_worked <= 0:
    print("Error: Hours worked must be greater than 0.")
elif labels <= 0:
    print("Error: Labels must be greater than 0.")
elif hours_worked > SHIFT_HOURS:
    print(f"Error: Hours worked cannot be more than {SHIFT_HOURS}.")
elif accuracy < 0 or accuracy > 100:
    print("Error: Accuracy must be between 0 and 100.")
else:
    # Calculations
    labels_per_hour = labels / hours_worked
    seconds_per_label = (hours_worked * SECONDS_PER_HOUR) / labels
    estimated_shift_labels = labels_per_hour * SHIFT_HOURS

    # Remaining shift calculations
    hours_remaining = SHIFT_HOURS - hours_worked

    # Target calculations
    if labels < DAILY_TARGET:
        labels_remaining = DAILY_TARGET - labels
        labels_above_target = 0
    else:
        labels_remaining = 0
        labels_above_target = labels - DAILY_TARGET

    # Required pace + pace status (computed once, reused for display)
    if hours_remaining > 0 and labels_remaining > 0:
        required_pace = labels_remaining / hours_remaining
        pace_difference = labels_per_hour - required_pace
        if pace_difference > 0:
            pace_status = f"{pace_difference:.0f} labels/hour ahead of required pace"
        elif pace_difference < 0:
            pace_status = f"{abs(pace_difference):.0f} labels/hour behind required pace"
        else:
            pace_status = "Exactly on required pace"
        pace_line = f"{required_pace:.0f} labels per hour"
    elif labels_remaining <= 0:
        required_pace = 0
        pace_status = "Target already achieved"
        pace_line = pace_status
    else:
        required_pace = 0
        pace_status = "Shift completed"
        pace_line = pace_status

    # Productivity
    if labels_per_hour >= EXCELLENT_THRESHOLD:
        productivity = "Excellent productivity"
    elif labels_per_hour >= GOOD_THRESHOLD:
        productivity = "Good productivity"
    elif labels_per_hour >= AVERAGE_THRESHOLD:
        productivity = "Average productivity"
    else:
        productivity = "Needs improvement"

    # Quality
    if accuracy >= QUALITY_THRESHOLD:
        quality = "Quality target achieved"
    else:
        quality = "Quality below target"

    # Target status
    if labels >= DAILY_TARGET:
        target_status = "Target achieved"
    else:
        target_status = f"{labels_remaining} labels needed"

    # Display results
    print("\n========== RESULTS ==========")
    print(f"Hello {name}!")
    print(f"Labels per hour: {labels_per_hour:.2f}")
    print(f"Seconds per label: {seconds_per_label:.2f}")
    print(f"Estimated {SHIFT_HOURS}hr labels: {estimated_shift_labels:.0f}")
    print(f"Hours remaining: {hours_remaining:.2f}")
    print(f"Labels remaining to target: {labels_remaining}")
    if labels_above_target > 0:
        print(f"Labels above target: {labels_above_target}")
    print(f"Required pace to target: {pace_line}")
    print(f"Target status: {target_status}")
    print(f"Pace comparison: {pace_status}")
    print(f"Productivity: {productivity}")
    print(f"Quality: {quality}")
    print("=============================")
