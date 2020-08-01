def between_markers(text: str, begin: str, end: str) -> str:
    begin_index = text.find(begin)
    end_index = text.find(end)
    result = ''
    for i in range(begin_index + 1, end_index):
        result += text[i]

    return result


text = "What is >apple<"
begin = ">"
end = "<"
print(between_markers(text,begin,end))