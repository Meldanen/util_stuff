def is_english_word(word):
    return word.lower() in words


with open("words.txt") as word_file:
    words = set(word.strip().lower() for word in word_file if len(word) == 6)

# example: nopes = ['d', 'i']
nopes = [] 
# example: yeps = [('l', 4), ('g', 2)] 
yeps = []  
# example: yeps_somewhere = [('a', [0]), ('r', [3, 2])]
yeps_somewhere = []  
final_words = []
and_back_to_start = False
for word in words:
    and_back_to_start = False
    if set(word).intersection(nopes):
        continue
    for yep_somewhere in yeps_somewhere:
        yep_somewhere_letter = yep_somewhere[0]
        yep_somewhere_but_not_here = yep_somewhere[1]
        if yep_somewhere_letter not in word:
            and_back_to_start = True
            break
        for i, letter in enumerate(word):
            if letter == yep_somewhere_letter:
                if i in yep_somewhere_but_not_here:
                    and_back_to_start = True
                    break

    if and_back_to_start:
        continue
    if len(yeps) > 0:
        for i, yep in enumerate(yeps):
            all_good = False
            if word[yep[1]] == yep[0]:
                if i == (len(yeps) - 1):
                    final_words.append(word)
                else:
                    continue
            else:
                break
    else:
        final_words.append(word)

print(final_words)
