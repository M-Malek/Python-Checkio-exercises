text = ""
begin = ""
end = ""

if not begin:
    begin_index = 0
elif not begin in text: 
    begin_index = 0
else:
    begin_index = text.find(begin) + len(begin)

if not end:
    end_index = len(text)
elif not end in text:
    end_index = len(text)
else:
    end_index = text.find(end)

print(text[begin_index:end_index])

#albo

if begin in text:
    begin_index = text.find(begin) + len(begin)
else:
    begin_index = 0

if end in text:
    end_index = text.find(end)
else:
    end_index = len(text)

#return text[begin_index:end_index]
print(text[begin_index:end_index])