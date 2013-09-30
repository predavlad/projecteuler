import time
import datetime

start_time = time.time()

varDate = datetime.datetime.strptime('1/1/1900', "%m/%d/%Y")
endDate = datetime.datetime.strptime('12/31/2000', "%m/%d/%Y")

varDate += datetime.timedelta(days=6)  # go to the first Sunday
counter = 0

while varDate < endDate:
    varDate += datetime.timedelta(days=7)
    # Sunday + first day of the month
    if varDate.weekday() == 6 and varDate.day == 1:
        print varDate.weekday(), varDate.day, varDate
        counter += 1


print counter  # for some reason python calculates 2 extra days it shouldn't

print time.time() - start_time, "seconds"
