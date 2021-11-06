string = "The text is a corrupted version version of the original"

def uniquify(string):
    output = []
    seen = set()
    for word in string.split():
        if word not in seen:
            output.append(word)
            seen.add(word)
    return ' '.join(output)


print(uniquify(string))
