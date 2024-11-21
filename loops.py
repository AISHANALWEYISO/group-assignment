#qtn 1
def even_numbers():
    for even in range(2,20,2):
        print(even)
even_numbers()        



#qtn 2
number = int(input("Enter a number: "))

while number <= 10:
    number = int(input("enter a number greater than 10: "))

print("number greater than 10")



#qtn 3
for i in range(1,11):
    for k in range(1,6):
        print(i*k, end= "\t")
    print("\n")   
          


#qtn4
list = [4, 7, 2, 9, 12, 15]
odd_sum =0 
for num in list:
    if num% 2 !=0:
        odd_sum+=num 
print(odd_sum)        

