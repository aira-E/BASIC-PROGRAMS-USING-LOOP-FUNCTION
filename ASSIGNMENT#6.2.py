#Number Sorter

#Get user's Input
first = int(input ("Enter the first number: "))
second = int(input ("Enter the second number: "))
third = int(input ("Enter the third number: "))
fourth = int (input ("Enter the fourth number: "))

#Smallest Number
def smallest_num (first,second,third,fourth):
    if first < second and first < third and first < fourth:
        smallest = first
    elif second < first and second < third and second < fourth:
        smallest = second
    elif third < first and third < second and third < fourth:
        smallest = third
    else:
        smallest = fourth
    return smallest
    
#Smaller Number
def smaller_num (first,second,third,fourth):
   if (first > second and first < third and first < fourth) or (first > third and first < second and first < fourth) or (first > fourth and first < third and first < second):
       smaller = first
   elif (second > first and second < third and second < fourth) or (second < first and second > third and second < fourth) or (second < first and second < third and second > fourth):
        smaller = second
   elif (third > first and third < second and third < fourth) or (third < first and third > second and third < fourth) or (third < first and third < second and third > fourth):
        smaller = third
   else:
        smaller = fourth
   return smaller

#Small Number
def small_num (first,second,third,fourth):
    if (first > second and first > third and first < fourth) or (first > second and first < third and first > fourth) or (first < second and first > third and first > fourth):
        small = first
    elif (second > first and second > third and second < fourth) or (second > first and second < third and second > fourth) or (second < first and second > third and second > fourth):
        small = second
    elif (third > first and third > second and third < fourth) or (third > first and third < second and third > fourth) or (third < first and third > second and third > fourth):
        small = third
    else:
        small = fourth
    return small

#Large Number
def large_num (first,second,third,fourth):
    if first > second and first > third and first > fourth:
        large = first
    elif second > first and second > third and second > fourth:
        large = second
    elif third > first and third > second and third > fourth:
        large = third
    else:
        large = fourth
    return large
    
first_num = smallest_num (first,second,third,fourth)
second_num = smaller_num (first,second,third,fourth)
third_num = small_num (first,second,third,fourth)
fourth_num = large_num (first,second,third,fourth)

#Display
print (f" Sorted number in ascending order: {first_num}, {second_num}, {third_num}, {fourth_num}")
