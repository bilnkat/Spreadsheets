txt = ""

emails = []

while txt.find('>') != -1:
    str1 = txt.find('<')
    str2 = txt.find('>')
    temptxt = txt[str1+1:str2]
    # print(temptxt)
    emails.append(temptxt)
    txt = txt[str2 + 1:]