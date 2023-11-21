import re

txt = "Test for end of the text."

x = re.search("^Test.*text.$", txt)
print(x)


txt = "ADSGAnieGDG aSnieDGag nie gaaniegf gafnieg fdag gfdagniefgadfgnie."

x = re.findall("nie", txt)
print(x)

x = re.sub("nie", "WOW", txt)
print(x)

x = re.findall(r"\bnie\b", txt)
print(x)

x = re.findall(r"[\w\.]+", txt)
print(1, x)

txt = "Test for end of the text."

x = re.split("\s", txt)
print(x)

mail = "adgag.gsdfgsd@pw.edu.pl"

x = re.split("@", mail)
print(x)

x = re.match("^[\w\.]+@[\w\.]+", mail)
print(bool(x))


txt = "Rok 2023 bedzie lepszy"

x = re.sub("\d", 'X', txt)
print(x)

kot = "Nasz kot ma 6 lat i wazy 4 kg."
x = re.findall(r"\d+", kot)
print(x)

x = re.search(r"^nasz", kot, re.IGNORECASE)
print(x)


phone = "Moj numer to 609-456-0986."
x = re.search(r"\b[0-9]{3}-\d{3}-\d{4}", phone)
print(x)

