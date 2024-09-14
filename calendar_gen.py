from icalendar import Calendar, Event
from datetime import datetime, timedelta

# Create a new calendar
cal = Calendar()

# Define event function for time blocks
def create_block(summary, start_time, end_time):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    return event

# Set the start date (Monday)
base_date = datetime(2024, 9, 16, 6, 30)

# Weekday schedule for Monday to Friday
for day in range(5):  # Monday to Friday
    day_offset = timedelta(days=day)

    # Meditation + Yoga (if applicable)
    if day % 2 == 0:  # Every other day yoga
        cal.add_component(create_block("Meditation + Yoga", base_date + day_offset, base_date + day_offset + timedelta(hours=1, minutes=30)))
    else:
        cal.add_component(create_block("Meditation", base_date + day_offset, base_date + day_offset + timedelta(minutes=40)))

    # Breakfast
    cal.add_component(create_block("Breakfast", base_date + day_offset + timedelta(minutes=40), base_date + day_offset + timedelta(hours=1)))

    # French Study Block
    cal.add_component(create_block("French Study", base_date + day_offset + timedelta(hours=1), base_date + day_offset + timedelta(hours=3)))

    # Work Block 1 (Projects work)
    cal.add_component(create_block("Projects Work", base_date + day_offset + timedelta(hours=3, minutes=15), base_date + day_offset + timedelta(hours=5, minutes=45)))

    # Lunch
    cal.add_component(create_block("Lunch", base_date + day_offset + timedelta(hours=5, minutes=45), base_date + day_offset + timedelta(hours=6, minutes=45)))

    # Work Block 2 (Job applications/Projects/French)
    cal.add_component(create_block("Work Block", base_date + day_offset + timedelta(hours=6, minutes=45), base_date + day_offset + timedelta(hours=9, minutes=15)))

    # Gym/Exercise (Running on dedicated day)
    if day == 2:  # Dedicated running day (Wednesday)
        cal.add_component(create_block("Running", base_date + day_offset + timedelta(hours=10), base_date + day_offset + timedelta(hours=12)))
    else:
        cal.add_component(create_block("Gym Workout", base_date + day_offset + timedelta(hours=10), base_date + day_offset + timedelta(hours=12)))

    # Dinner
    cal.add_component(create_block("Dinner", base_date + day_offset + timedelta(hours=12), base_date + day_offset + timedelta(hours=13)))

# Weekend schedule (Saturday/Sunday)
for day in range(5, 7):  # Saturday and Sunday
    day_offset = timedelta(days=day)

    # Meditation
    cal.add_component(create_block("Meditation", base_date + day_offset, base_date + day_offset + timedelta(minutes=40)))

    # Breakfast
    cal.add_component(create_block("Breakfast", base_date + day_offset + timedelta(minutes=40), base_date + day_offset + timedelta(hours=1)))

    # Groceries and Meal Prepping
    if day == 5:  # Saturday - Groceries
        cal.add_component(create_block("Groceries", base_date + day_offset + timedelta(hours=2), base_date + day_offset + timedelta(hours=3, minutes=30)))
    elif day == 6:  # Sunday - Meal Prepping
        cal.add_component(create_block("Meal Prepping", base_date + day_offset + timedelta(hours=2), base_date + day_offset + timedelta(hours=5)))

# Write to .ics file
with open('schedule_discipline_maybe.ics', 'wb') as f:
    f.write(cal.to_ical())
