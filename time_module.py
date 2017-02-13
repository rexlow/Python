#Unix Epoch Time
# This is the format you should get timestamps in for saving in databases.
# It is a simple floating point number that can be converted to an integer.
# It is also good for arithmetic in seconds, as it represents the number
# of seconds since Jan 1, 1970 00:00:00,
# and it is memory light relative to the other representations of time

import time
from datetime import datetime

x = time.time()
print("Epoch time " + str(x))

#ctime
print("ctime " + time.ctime(x))

#datetime
y = datetime.now()
print("datetime.now() " + str(y))

#utcnow
utc_time = datetime.utcnow()
print(utc_time)
