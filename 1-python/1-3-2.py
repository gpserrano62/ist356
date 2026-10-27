#code pre-function
string = ("Hello, World!")
string2 = string.replace("!","").replace(",","").replace("?","")
print(string2)
print(string)

# write above as a function
def clean_string(input_string: str) -> str:

    text2 = text
    for char in ["!", ",", "?"]:
        text2 = text2.replace(char, "")
        text3 = text2.strip()
        text4 = text3.lower()
        return text4

    text = "Hello, World!    "
    expected_output = clean_text(text)
    print(text)
    print(cleaned_text)
    