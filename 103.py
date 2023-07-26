from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz
# import jdatetime

today = str(JalaliDate.today()).split("-")
today = [int(i) for i in today]
# hour = str(jdatetime.datetime.now()).split()[1][:5]
# print(hour)
date = JalaliDateTime(today[0], today[1], today[2], 20, 3, 0, 0, pytz.utc).strftime("%d")
print(date)
