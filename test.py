time = input('Enter the number of seconds \n')
float_time = float(time)
Minutes = float_time//60
Hours = float_time//3600
floor_minutes = float_time%60
floor_hours = float_time%3600
str_time = str(float_time)
str_minutes = str(Minutes)
str_Hours = str(Hours)
str_floor_minutes = str(floor_minutes)
str_floor_hours = str(floor_hours)
print('The number of seconds is' + ' ' +  str_time)
print('The number of minutes is' + ' ' +  str_minutes)
print('And the remainder of dividing the minutes is' +' '+  str_floor_minutes)
print('The number of hours is'  + ' ' + str_Hours)
print('And the remainder of dividing the hours is'  + ' ' + str_floor_hours)








