# compares strings right-to-left
def compare(x, y):
    if len(x) < len(y):
        shorter = len(x)-1
    else:
        shorter = len(y)-1

    # go through each character in the pair, comparing them, and return a value accordingly
    while shorter != -1:
        if x[shorter] == y[shorter] or 26 <= ord(x[shorter])-97 < 0 or 26 <= ord(y[shorter])-97 < 0:
            shorter -= 1
        elif x[shorter] < y[shorter]:
            return -1
        else:
            return 1

    return 0


# sorts a list of strings across 26 containers, one for each letter of the alphabet (the letter the string ends with)
def initial_sort(url_list):
    return_list = [[] for _ in range(26)]
    for x in url_list:
        return_list[ord(x[len(x)-1])-97].append(x)

    return return_list


# program accepts list of URLS and sorts them from left to right
input_list = []

n = input("")

while n != "":
    input_list.append(n)
    n = input("")

containers = initial_sort(input_list)

# use compare() to sort strings in each container
for c in containers:
    i = 0
    while i < len(c):
        j = 0
        while j < len(c)-1:
            if compare(c[j], c[j+1]) > 0:
                temp = c[j+1]
                c[j+1] = c[j]
                c[j] = temp
            j += 1
        i += 1

# printed sorted list
for c in containers:
    for e in c:
        print(e)
#hi