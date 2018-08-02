"'# TAKING THE INPUT'"
S = input()
VOWELS = 0
"'#CHECKING THE THE RANGE'"
for char in S:
    if char in'aeiou':
        VOWELS = VOWELS + 1

print(VOWELS)
 