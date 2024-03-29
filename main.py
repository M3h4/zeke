from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < total_seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = total_seconds - time_elapsed
        hours_left = time_left // 3600
        minutes_left = (time_left % 3600) // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Your alarm will be off in {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3.mp3")

# Get input from the user for hours, minutes, and seconds.
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

# Call the alarm function with the provided time.
alarm(hours, minutes, seconds)
