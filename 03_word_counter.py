# how to split a string

text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
        "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and "
        "scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into "
        "electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of "
        "Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like "
        "Aldus PageMaker including versions of Lorem Ipsum.")

# Triple quote string """ """ allow to have multiple string listed as one big string

# print(text)
# len(text) - counts the number of chracters
# counting how many times a word / character reapeats in the splited data
#  setting all to lower case before spliting
text_list = text.lower().split()
print(text_list)

word_count = {}

for word in text_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
