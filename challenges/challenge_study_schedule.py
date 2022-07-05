def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for entry_time, exit_time in permanence_period:
            if entry_time <= target_time <= exit_time:
                count += 1
        return count
    except TypeError:
        return None
