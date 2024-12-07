
def count_words(sentence):
    try:
        assert sentence != '', "Empty sentence provided"
        word_count = {}
        words = sentence.split()
        for word in words:
            word = word.lower().strip(",.!?")  # Normalize word
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1  # Incorrect modification of global variable
        sorted_word_count = dict(sorted(word_count.items(),key = lambda x: -x[1]))
        return sorted_word_count
    except AssertionError as e:
        print(e)
    finally:
        pass
sentence = "This is a test. This test is only a test."
if sentence != '':
    print(count_words(sentence))
