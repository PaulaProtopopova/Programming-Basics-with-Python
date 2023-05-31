import math

record_to_beat_seconds = float(input())
meters_to_swim = float(input())
seconds_per_meter = float(input())

planned_lateness = math.floor(meters_to_swim / 15) * 12.5
personal_record_seconds = (seconds_per_meter * meters_to_swim) + planned_lateness


if personal_record_seconds < record_to_beat_seconds:
    print(f'Yes, he succeeded! The new world record is {personal_record_seconds:.2f} seconds.')

else:
    diff = personal_record_seconds - record_to_beat_seconds
    print(f'No, he failed! He was {diff:.2f} seconds slower.')