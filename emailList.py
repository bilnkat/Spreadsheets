def listEmails():

    f = open(r"C:\Users\bgeneral\Desktop\email.txt", "r")
    txt = f.read()

    emails = []

    while txt.find('>') != -1:
        str1 = txt.find('<')
        str2 = txt.find('>')
        temptxt = txt[str1+1:str2]
        # print(temptxt)
        emails.append(temptxt)
        txt = txt[str2 + 1:]

    return emails