
print()
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      #    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
      #   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:step]
print(my_list)
print(my_list[5])
print(my_list[0])
print(my_list[-1])
print(my_list[-10])
print(my_list[0:6]) # prints 0 to 5
print(my_list[3:8]) # prints 3 to 7
print(my_list[-7:-2]) # prints 3 to 7
# You can also Mix the Positive and Negative numbers
print(my_list[1:-2]) # prints 1 to 7
print(my_list[1:]) # prints 1 to end
print(my_list[5:]) # prints 1 to end 9
print(my_list[:-1]) # prints 0 to end 8
print(my_list[:]) # prints 0 to end
print(my_list[2:-1:2]) # prints 2 to 9 and skips 1
print(my_list[2:-1:-1]) # prints 2 to 9 and skips 1
print(my_list[-1:2:-1])
print(my_list[-2:2:-1])
print(my_list[-2:1:-2])
print(my_list[::-1])

print('===========String Slicing==========')
sample_url = 'http://coreyms.com'
print()
print(sample_url)
# Reverse the url
print(sample_url[::-1])
# Get the Top level domain
print(sample_url[-4:])
# print the url without the https://
print(sample_url[7:])
# print the url without the htts:// or the top level domain
print(sample_url[7:-4])

