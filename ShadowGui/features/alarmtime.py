import datetime
import os
from pygame import mixer
from pygame.locals import *
import time


def playmusic():
    # music_dir = 'D:\\Audio' # music directry path 
    # os.startfile(os.path.join(music_dir,'AI_alarm05.mp3'))
    os.startfile(r"D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\AI_alarm05.mp3") # add your requirements

def alaramplay():

	def check_alarm_input(alarm_time):
		"""Checks to see if the user has entered in a valid alarm time"""
		if len(alarm_time) == 1: # [Hour] Format
			if alarm_time[0] < 24 and alarm_time[0] >= 0:
				return True
		if len(alarm_time) == 2: # [Hour:Minute] Format
			if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
			alarm_time[1] < 60 and alarm_time[1] >= 0:
				return True
		elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
			if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
			alarm_time[1] < 60 and alarm_time[1] >= 0 and \
			alarm_time[2] < 60 and alarm_time[2] >= 0:
				return True
		return False

	# Get user input for the alarm time
	print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
	while True:
		alarm_input = input(">> ")
		try:
			alarm_time = [int(n) for n in alarm_input.split(":")]
			if check_alarm_input(alarm_time):
				break
			else:
				raise ValueError
		except ValueError:
			print("ERROR: Enter time in HH:MM or HH:MM:SS format")

	# Convert the alarm time from [H:M] or [H:M:S] to seconds
	seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
	alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

	# Get the current time of day in seconds
	now = datetime.datetime.now()
	current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

	# Calculate the number of seconds until alarm goes off
	time_diff_seconds = alarm_seconds - current_time_seconds

	# If time difference is negative, set alarm for next day
	if time_diff_seconds < 0:
		time_diff_seconds += 86400 # number of seconds in a day

	# Display the amount of time until the alarm goes off
	print(f"Alarm set to go off in {datetime.timedelta(seconds=time_diff_seconds)}")

	# Sleep until the alarm goes off
	time.sleep(time_diff_seconds)

	# Time for the alarm to go off
	print("Wake Up!")
	playmusic()

if __name__ == '__main__':
	alaramplay()
