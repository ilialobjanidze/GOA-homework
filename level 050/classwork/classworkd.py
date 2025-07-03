def format_duration(seconds):
    if seconds == 0:
        return "now"
    time_units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]

    components = []
    for unit_name, unit_seconds in time_units:
        if seconds >= unit_seconds:
            unit_value = seconds // unit_seconds
            seconds %= unit_seconds
            components.append(f"{unit_value} {unit_name}" + ("s" if unit_value > 1 else ""))

    if len(components) > 1:
        return ", ".join(components[:-1]) + " and " + components[-1]
    else:
        return components[0]
    


