def words_order(text: str, words: list):
    text = text.split(" ")
    check_list = []
    j = 0
    for i in words:
        if words.count(i) >= 2:
            return False

    if len(words) == 1:
        for i in text:
            if i == words[0]:
                check_list.append(i)
                break
    else:
        for i in text:
            if j > len(words)-1: 
                pass
            elif i == words[j]:
                check_list.append(i)
                j += 1

    if check_list == words:
        return True
    else:
        return False


text = "london in the capital of great britain"
words = ["london","great"]
print(words_order(text, words))
