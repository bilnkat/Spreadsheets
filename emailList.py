def listOfEmails(distroFile):

    f = open(distroFile, "r")
    txt = f.read()

    emails = []

    while txt.find('>') != -1:
        str1 = txt.find('<')
        str2 = txt.find('>')
        tmp = txt[str1+1:str2]
        emails.append(tmp)
        txt = txt[str2 + 1:]

    return emails

e = listOfEmails(r'C:\Users\bgeneral\Desktop\email.txt')
print(e, file=open(r"C:\Users\bgeneral\Desktop\output.txt", "a"))
