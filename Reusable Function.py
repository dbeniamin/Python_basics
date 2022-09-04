def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒",
        ":D": "😁"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
# function should not contain "input" and "output" part of a code
# code converted to function so it can be use again def -> definig the function
