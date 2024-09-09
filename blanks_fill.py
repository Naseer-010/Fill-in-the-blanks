
def fill_blanks(paragraph, words):
    # Splitting paragraph into sentences based on period followed by space
    sentences = paragraph.split('. ')

    filled_paragraph = ""
    word_index = 0

    for sentence in sentences:
        words_in_sentence = sentence.split()
        for i in range(len(words_in_sentence)):
            if '_____' in words_in_sentence[i]:
                if word_index < len(words):
                    words_in_sentence[i] = words[word_index]
                    word_index += 1
                else:
                    print("Not enough words provided to fill all blanks.")
                    return

        filled_sentence = ' '.join(words_in_sentence)
        filled_paragraph += filled_sentence + '. '

    return filled_paragraph


paragraph1 = "Upon arrival at the school, the students are sorted into one of four houses—Gryffindor, Hufflepuff, Ravenclaw, \
 or Slytherin. Harry ends up in _____, and during his eventful first year at Hogwarts he becomes close friends with two \
 other members of the house, Ron Weasley, who comes from an old wizarding family, and _____ Granger, whose parents are \
 Muggles (those who are not magical). Harry also finds that he has an enemy  Draco Malfoy ( in _____ ). In addition, \
 Harry's prowess in flying on a broomstick makes him a star of Gryffindor's Quidditch team. Hoping to get Harry and his \
 friends into trouble, _____ tricks them into leaving their rooms one night, a violation of school rules. While trying to \
 avoid being caught, they discover a three-headed _____ guarding a trapdoor. Harry gradually comes to the conclusion that \
 Professor Snape, who teaches Potions, dislikes him intensely and is trying to get hold of whatever is behind the trapdoor. \
 Harry receives his father's cloak of invisibility as a christmas gift, and, while exploring under the cloak's cover, he finds\
 the Mirror of Erised, in which he can see his parents. Later, headmaster Albus _____ explains that the mirror \
 shows the viewer's deepest desire."

paragraph2 = "Upon arrival at the _____ school, the students are sorted into one of four houses - Gryffinder, Huffelpuff, \
Ravenclaw or slytherin. Harry ends up in _____ house and he became close friends with two other members of the same house, \
Ron Weasley and _____. He also finds that he has an enemy named _____ in _____ house."

print("The paragraph is about Harry Potter try to answer it considering this")


print("Original Paragraph:")
print(paragraph2)
print("Total 5 blanks")

words = input("Enter words to fill in blanks (comma-separated): ").strip().split(',')
filled_paragraph = fill_blanks(paragraph2, words)

if filled_paragraph:
    print("\nFilled Paragraph:")
    print(filled_paragraph)



















