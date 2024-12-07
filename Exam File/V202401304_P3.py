def transform_string(text):
    try:
        assert text.isdigit() == False, 'Non-alphabetical character found.'
        assert text != '', 'Empty String'
        count = 0
        new_string = []
        for i, char in enumerate(text):
            if i%2==0:
                new_string.append(char.upper())
            else:
                new_string.append(char.lower())
        for i in range(len(new_string)):
            if new_string[i] in ['u','e','o','a','i','U','E','O','A','I']:
                new_string[i] = '*'
                count+=1
        saved_new_string = ''.join(new_string)
        new_dict = {
            "original": text,
            "transformed": saved_new_string,
            "vowel_count": count
        }
        return new_dict
    except AssertionError as d:
        print(d)
    finally:
        pass
text = "Hello123"
print(transform_string(text))
