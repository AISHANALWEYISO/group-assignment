#qtn 1
student={
    "name":"Alice",
    "Age":25,
    "Grade":"B",
}
for key,value in student.items():
    print(f"{key}:{value}")


#qtn2    
def names_and_age(details):
    adults = [names for names, age in details.items() if age >= 21]
    return adults
details= {'Alice': 24,
            'Bob': 19, 
            'Charlie': 30
            }

adults = names_and_age(details)
print(adults)


#qtn3
prices= {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items = ['apple', 'orange', 'banana', 'banana']
total_cost  = 0
for item in items:
    total_cost += prices.get(item,0)
print(total_cost)

#qtn 4
sentence = "hello world hello"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)