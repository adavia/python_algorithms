def convert_html(st):
    lst = list(st)
    mapper = {
        '&': '&​amp;',
        '<': '&​lt;',
        '>': '&​gt;',
        '"': '&​quot;',
        '\'': '&​apos;'
    }

    for i in range(len(lst)):
        if lst[i] in mapper:
            lst[i] = mapper[lst[i]]

    return ''.join(lst)

print(convert_html('Dolce & Gabbana'))
print(convert_html('Hamburgers < Pizza < Tacos'))
print(convert_html('Stuff in "quotation marks"'))
print(convert_html("Schindler's List"))
print(convert_html('<>'))
print(convert_html('abc'))
