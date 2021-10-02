# import time

# The time() function returns the number of seconds passed since epoch.

# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).
# code:
# seconds = time.time()
# print("Seconds since epoch =", seconds)

# The time.ctime() function takes seconds passed since epoch as an argument and returns a string representing local time.
# code:
# seconds passed since epoch
# seconds = 1545925769.9618232
# local_time = time.ctime(seconds)
# print("Local time:", local_time)

# The sleep() function suspends (delays) execution of the current thread for the given number of seconds.
# code:
# print("This is printed immediately.")
# time.sleep(2.4)
# print("This is printed after 2.4 seconds.")

# The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in local time.
# code:
# result = time.localtime(1545925769)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.
# code:
# result = time.gmtime(1545925769)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# The mktime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and returns the seconds passed since epoch in local time. Basically, it's the inverse function of localtime().
# code:
# t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
#
# local_time = time.mktime(t)
# print("Local time:", local_time)

# The asctime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and returns a string representing it. Here's an example:
# code:
# t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
#
# result = time.asctime(t)
# print("Result:", result)

# The strftime() function takes struct_time (or tuple corresponding to it) as an argument and returns a string representing it based on the format code used. For example,
# code:
# named_tuple = time.localtime() # get struct_time
# time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
#
# print(time_string)

# The strptime() function parses a string representing time and returns struct_time.
# code:
# time_string = "21 June, 2018"
# result = time.strptime(time_string, "%d %B, %Y")
#
# print(result)