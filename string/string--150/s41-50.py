#----------------------------->
# 41Check if a string contains a substring (without using built-in method). S1 = "Hello", Sub="ell" TRUE
s= input("enter the string :")
s2 = input("enter if its a substring :")

for i in range(len(s)):

    for j in range(len(s2)):
        if s2[j]==s[i]
# 42Check if two strings are equal without equals(). S1 = "abc", S2 = "abc" TRUE
# 43Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE
# 44Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE
# 45Check whether a string starts/ends with another string. S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True
# 46Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE
# 47Check for substring using concatenation trick. S1="CDAB", S2="ABCD" True (S1 is in S2+S2)
# 48Remove all vowels. S = "aeiou XYZ" " XYZ"
# 49Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple" "ap*le" (or similar output depending on implementation)
# 50Remove all digits. S = "a1b2c3" "abc"
# 51Extract only digits. S = "a1b2c3" "123"
# 52Remove all special characters. S = "a!@b#c" "abc"
# 53Remove punctuation. S = "Hello, world!" "Hello world"
# 54Replace duplicate chars with '$'. S = "hello" "he$lo"
# 55Reverse only vowels. S = "hello" "holle"
# 56Reverse only consonants. S = "apple" "eplpa"
# 57Merge two strings alternatively. S1 = "ABC", S2 = "def" "AdBeCf"
# 58Rotate characters left by 2 positions. S = "abcde" "cdeab"
# 59Rotate characters right by 3 positions. S = "abcde" "cdeab"
# 60Append two strings but remove adjacent duplicates. S1="miss", S2="issippi" "misisipi"



# 61Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1
# 62Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3
# 63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2
# 64Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)
# 65Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)
# 66Count number of sentences in a paragraph. P = "This. Is. Test." 3
# 67Count how many times a substring appears. S = "abab", Sub = "ab" 2
# 68Count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3)
# 69Count how many times 'life' appears in a string. S = "life is life" 2
# 70Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis)
# 71Print all substrings. S = "abc" "a, b, c, ab, bc, abc"
# 72Print all substrings of length n. S = "abc", n = 2 "ab, bc"
# 73Find the longest palindromic substring. S = "babad" "bab" (or "aba")
# 74Find the longest substring without repeating characters. S = "abcabcbb" "abc"
# 75Find the longest common prefix among strings. Strings = ["flower", "flow", "flight"] "fl"
# 76Find the longest common suffix among strings. Strings = ["baking", "making", "taking"] "king"
# 77Find the longest substring that appears at both ends. S = "abracadabra" "abra"
# 78Find the longest mirror-image substring at both ends. S = "aabccbaa" "aab"
# 79Divide a string into n equal parts. S = "abcdef", n = 3 "ab", "cd", "ef"
# 80Print list items containing all characters of a given word. List = ["apple", "plea"], Word = "pal" "apple", "plea"
# 81Generate a hash code or UUID. S = "test" Hash: 3556498 (Example hash code)
# 82Create a string from a character array. Char[] = {'h', 'i'} "hi"
# 83Create a string from a byte array. Byte[] = {72, 101, 108} (ASCII for H, e, l) "Hel"
# 84Print ASCII value of each character. S = "A" A: 65
# 85Convert string into a char array without built-in functions. S = "test" {'t', 'e', 's', 't'}
# 86Print all permutations of a string without repetition. S = "ab" "ab", "ba"
# 87Print all permutations of a string with repetition. S = "aab" "aab", "aba", "baa"
# 88Rearrange a string so that identical characters are at least d distance apart. S = "aaabc", d = 2 "abaca"
# 89Remove 'b' and 'ac' from a string. S = "abacbb" "c"
# 90Remove adjacent duplicates recursively. S = "azxxzy" "ay"
# 91Check if two strings are interleaving of another string. S1 = "aab", S2 = "axy", S3 = "aaxaby" TRUE
# 92Check if two strings are pq-balanced. S1 = "pqqp", S2 = "qpqp" Example dependent on specific "pq-balanced" definition
# 93Match strings with wildcard characters ($\*$, ?). Pattern = "a?c", Text = "axcde" TRUE
# 94Find the smallest window containing all characters of another string. S1 = "ADOBECODEBANC", S2 = "ABC" "BANC"
# 95Find the second most frequent character. S = "aabbccdde" c' or 'd'
# 96Find the second most frequent word. S = "a b a c b" c'
# 97Check if two given strings appear at the end of each other (ignoring case). S1 = "abc", S2 = "Xabc" TRUE
# 98Check if the first 'z' is immediately followed by another 'z'. S1 = "zzyy", S2 = "zyzz" S1: True, S2: False
# 99Check if a 'z' is happy (surrounded by same chars). S = "azzb" FALSE
# 100Return true if string contains 'abc' not followed by '.'. S1 = "abcx", S2 = "abc." S1: True, S2: False
