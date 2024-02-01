count = 0
pattern = []
text = []
test_case = int(input("Enter test cases: "))
# accepting user input
# first accepting number of test cases and for each test case, accepting pattern and text
while(count < test_case):
    pattern_var = input("Enter pattern: ")
    pattern.append(pattern_var)
    text_var = input("Enter text: ")
    text.append(text_var)
    count = count + 1

n = len(pattern)

# loop through array to match pattern(in reverse order as well) and text
for x in range(n):
     if pattern[x] in text[x] or pattern[x][::-1] in text[x]:
         print ("YES")
     else:
         print("NO")