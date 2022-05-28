def find_anagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
         print("True")
    else:
        print("False")
s1 = "rescue"
s2 = "secure"
find_anagram(s1, s2)
