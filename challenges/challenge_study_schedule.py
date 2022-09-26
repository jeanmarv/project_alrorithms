def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for key, value in permanence_period:
            if target_time >= key and int(target_time) <= value:
                counter += 1
        return counter
    except TypeError:
        return None