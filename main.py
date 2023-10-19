import re
import numpy as np
from sklearn.ensemble import IsolationForest

def ReadData(path):
	df = np.array([["IP", "Date", "Request", "Status", "Referrer", "User Agent", "Time"]])

	# Define a regular expression pattern to match IP, date, request, status, and user agent
	pattern = r'(?P<ip>[\d\.]+) - - \[(?P<date>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) \d+ "(?P<referrer>[^"]+)" "(?P<user_agent>[^"]+)" (?P<time>\d+)'

	with open(path, "r") as data:
		for log_entry in data:
			# Use re.search to find the pattern in the log entry
			match = re.search(pattern, log_entry)

			if match:
			    # Extract specific information from the match object
			    ip = match.group('ip')
			    date = match.group('date')
			    request = match.group('request')
			    status = match.group('status')
			    referrer = match.group('referrer')
			    user_agent = match.group('user_agent')
			    time = match.group('time')

			    new_log = np.array([[ip, date, request, status, referrer, user_agent, time]])

			    df = np.concatenate((df, new_log), axis=0)
			else:
			    print("No match found.")
		return df

if __name__ == "__main__":
	df = ReadData("./Data/logfiles.log")
	print(df[0])
