heights=[88, 102, 105, 99, 101]
print("heights of customers in inches is",heights)
newlist=[each_value_in_list*2.54 for each_value_in_list in heights]
print("height of customers in centimeters is",newlist)