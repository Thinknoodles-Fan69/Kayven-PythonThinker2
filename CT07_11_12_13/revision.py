
# Write a program to find the largest and smallest numbers in 
# a list using 
# 1a. max()
# 1b. min()
# 1c. without using max()
# 1d. without using min()
# 1e. find the sum of all the numbers
# 1f. find the count of items in the list
# 1g. find the average of all the numbers
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

####################################################
# Answer for Question 1a here
maxnum = max(list1)
# print(f"The biggest number is {maxnum}")

####################################################
# Answer for Question 1b here
minnum = min(list1)
# print(f"The smallest number is {minnum}")

####################################################
# Answer for Question 1c here

maxnum = 0
for num1 in list1:
    if num1 > maxnum:
        maxnum = num1

# print(maxnum)


####################################################
# Answer for Question 1d here

minnum = 9999
for num1 in list1:
    if num1 < minnum:
        minnum = num1

# print(minnum)


####################################################
# 1e. find the sum of all the numbers
total = 0
for i in list1:
    total += i

# print(total)



####################################################
# 1f. find the count of items in the list

# print(len(list1)) 


####################################################
# 1g. find the average of all the numbers

total = 0
for i in list1:
    total += i
average = total/ len(list1)

# print(average)


######################################################
# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# Answer for Question 2 here

# max = max(swim_times)
# min = min(swim_times)

# Man = 0
# for num1 in swim_times:
#     if num1 > Man:
#         Man = num1

# Mint = 999
# for num1 in swim_times:
#     if num1 < Mint:
#         Mint = num1

# count = 1
# for i in swim_times:
#     if Man != i:
#         count += 1
#     else:
#         print(f"The fastest swimmer is lane {count} with a time of {swim_times[count-1]}")
        
# count = 1
# for i in swim_times:
#     if Mint != i:
#         count += 1
#     else:
#         print(f"The slowest swimmer is lane {count} with a time of {swim_times[count-1]}")








#################################################################
# Question 4: 
# A bookstore keeps track of their sales figures each day 
# for the month of June. The sales for the 30 days are provided 
# in the list below. Find the days with the highest and lowest sales. 
# Assume that the first item in the list corresponds to Day 1.

# Find the total sales figure for the month
# Find the average sales rounded to 2 decimal points
#################################################################
daily_sales = [120, 98, 135, 105, 150, 112, 80, 130, 95, 110, 
               102, 85, 140, 99, 123, 145, 78, 90, 136, 145, 
               132, 108, 75, 88, 142, 115, 97, 121, 89, 100]
# Answer for Question 4 here


Man = 0
for num1 in daily_sales:
    if num1 > Man:
        Man = num1

Mint = 999
for num1 in daily_sales:
    if num1 < Mint:
        Mint = num1

count = 1
for i in daily_sales:
    if Man != i:
        count += 1
    else:
        print(f"The most amount to moolah earn is day {count} with a amount of {daily_sales[count-1]}")
        
count = 1
for i in daily_sales:
    if Mint != i:
        count += 1
    else:
        print(f"The least amount to moolah earn is day {count} with a amount of {daily_sales[count-1]}")




total = 0
for i in daily_sales:
    total += i

print(total)

average = total/len(daily_sales)
print(average)




##################################################################
# Question 5: 
# Hourly temperature measurements (°C) for a specific day are given below. 
# Write Python code to determine the highest and lowest temperatures, 
# along with the corresponding hour of measurement. 
# (First measurement at index 0 corresponds to midnight, 
#  and each subsequent value is measured hourly.)

# Find the average temperature for this day.
##################################################################
hourly_temperatures = [26.4, 25.9, 25.1, 24.6, 24.2, 23.8, 24.5, 25.6, 
                       27.3, 29.0, 30.5, 31.2, 32.0, 33.1, 32.8, 31.6,
                       30.8, 29.4, 28.1, 27.5, 27.0, 26.8, 26.0, 25.7]
# Answer for Question 5 here

Man = 0
for num1 in hourly_temperatures:
    if num1 > Man:
        Man = num1

Mint = 999
for num1 in hourly_temperatures:
    if num1 < Mint:
        Mint = num1

count = 1
for i in hourly_temperatures:
    if Man != i:
        count += 1
    else:
        print(f"The most temperature is hour {count} with temperature of {hourly_temperatures[count-1]}")
        
count = 1
for i in hourly_temperatures:
    if Mint != i:
        count += 1
    else:
        print(f"The smallest temperature is hour {count} with temperature of {hourly_temperatures[count-1]}")

total = 0
for i in hourly_temperatures:
    total += i


average = round(total/len(hourly_temperatures), 0)
print(average)
# decimals = average - int(average) 
# real_decimal = 0
# if decimals >= 0.5:
#     real_decimals = 1
# else:
#     real_decimals = 0

# real_average = real_decimals + int(average)
# print(real_average)



suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']
