def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_year = is_leap(year)
  print(leap_year)
  month -= 1
  if leap_year:
    if month_days[month] == month_days[1]:
      print(month_days[month] + 1)
      return
        
    print(month_days[month])
  else:
    print(month_days[month])


  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
# print(days)







