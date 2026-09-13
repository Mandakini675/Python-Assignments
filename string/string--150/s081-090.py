# 81Generate a hash code or UUID. S = "test" Hash: 3556498 (Example hash code)

# s = input("Enter the string: ")
# print(hash(s))

#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 82Create a string from a character array. Char[] = {'h', 'i'} "hi"
# char = input("Enter the string: ")
# s = "".join(char)
# print(s)

#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 83Create a string from a byte array. Byte[] = {72, 101, 108} (ASCII for H, e, l) "Hel"
# s = int(input("enter the string:"))
# s = list(map(int, input("Enter the bytes: ").split()))
# new = ""
# for ch in s:
#     new+=chr(ch)
# print(new)

#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 84Print ASCII value of each character. S = "A" A: 65
# char = input("enter string character:")
# print(ord(char))

#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 85Convert string into a char array without built-in functions. S = "test" {'t', 'e', 's', 't'}
# s = input("enter string:")
# arr=[]
# for c in s:
#     arr.append(c)
# print(arr)

#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 86Print all permutations of a string without repetition. S = "ab" "ab", "ba"
s = input("Enter the string: ")

def permutate(s, curr, used):
    
    # Base case
    if len(curr) == len(s):
        print(curr)
        return

    # Try every character
    for i in range(len(s)):
        
        if used[i]:
            continue

        # Choose
        used[i] = True
        curr += s[i]

        # Explore
        permutate(s, curr, used)

        # Backtrack / Undo
        curr = curr[:-1]
        used[i] = False


used = [False] * len(s)

permutate(s, "", used)

#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 87Print all permutations of a string with repetition. S = "aab" "aab", "aba", "baa"
s = input("Enter the string: ")

def permutate(s, curr):
    
    if len(curr) == len(s):
        print(curr)
        return

    for i in range(len(s)):
        curr += s[i]

        permutate(s, curr)

        curr = curr[:-1]


permutate(s, "")


#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 88Rearrange a string so that identical characters are at least d distance apart. S = "aaabc", d = 2 "abaca"



#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 89Remove 'b' and 'ac' from a string. S = "abacbb" "c"

#~~~~~~~~~~~~~~~~~~~~~~~~~>
# 90Remove adjacent duplicates recursively. S = "azxxzy" "ay"

#~~~~~~~~~~~~~~~~~~~~~~~~~>