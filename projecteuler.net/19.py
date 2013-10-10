import time
import datetime

start_time = time.time()

varDate = datetime.datetime.strptime('1/1/1900', "%m/%d/%Y")
endDate = datetime.datetime.strptime('12/31/2000', "%m/%d/%Y")

varDate += datetime.timedelta(days=6)  # go to the first Sunday
counter = 0

while varDate < endDate:
    varDate += datetime.timedelta(days=7)
    if varDate.weekday() == 6 and varDate.day == 1:
        counter += 1


print counter

print time.time() - start_time, "seconds"
