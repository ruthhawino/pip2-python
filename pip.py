
#1. Write a Python program to get a single string from two given strings, separated by a space,
#and swap the first two characters of each string

def swap_strings(str1, str2):
    str1_first_two = str1[:2]
    str2_first_two = str2[:2]
    new_str1 = str2_first_two + str1[2:]
    new_str2 = str1_first_two + str2[2:]
    
    result = new_str1 + ' ' + new_str2
    
    return result

str1 = "hello"
str2 = "world"
result = swap_strings(str1, str2)
print(result)

#2.Write a Python function that takes a list of words and returns the longest word 
#and the length of the longest one



def find_longest_word(words):
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word, max_length

words = ["apple", "banana", "cherry", "date", "elderberry"]
longest_word, length = find_longest_word(words)
print("The longest word is '{}' with length {}.".format(longest_word, length))


#3.Write a Python program that accepts a comma-separated sequence of words
#as input and prints the distinct words in sorted form (alphanumerically).


def sort_words(words):

    word_list = words.split(',')
    
    word_list = [word.strip() for word in word_list]
    
    distinct_words = sorted(set(word_list))
    
    result = ', '.join(distinct_words)
    
    return result

words = "apple, pear, orange, banana, pear, apple, kiwi"
result = sort_words(words)
print(result)



#4.Write a Python function that takes two lists and returns True if they have at least one common member.


def has_common_member(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    return bool(set1.intersection(set2))

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list3 = [9, 10, 11, 12]

print(has_common_member(list1, list2)) 
print(has_common_member(list1, list3)) 


#5Write a Python program to convert a list to a list of dictionaries.
#Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]


def list_to_dict(keys, values):
    
    result = []
    
    
    for i in range(len(keys)):
     current_dict = {keys[i]: values[i]}
        
    result.append(current_dict)
    
    return result
keys = ["Black", "Red", "Maroon", "Yellow"]
values = ["#000000", "#FF0000", "#800000", "#FFFF00"]
result = list_to_dict(keys, values)
print(result)


#6 Write a Python program to check whether all dictionaries in a list are empty or not

def all_empty(dicts):
    
    for d in dicts:
        
        if d:
            return False
    
    return True

list1 = [{}, {}, {}]
list2 = [{}, {"key": "value"}, {}]

print(all_empty(list1)) 
print(all_empty(list2))

numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]

evens = [num for num in numbers if num % 2 == 0]

print(evens)


# 7 Given a list of numbers, use list comprehension to remove all odd numbers from the list:
numbers = [3,5,45,97,32,22,10,19,39,43] 






























