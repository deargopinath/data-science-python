# 3.
# Weather forecasting organization wants to show is it day or night. 
# So	 write a program for such organization to find whether is it dark outside or not.
# Hint: Use time module.

import datetime
HH = datetime.datetime.now().hour
if (HH < 6) or (HH > 18):
    print ("Dark outside")
else:
    print ("Bright outside")