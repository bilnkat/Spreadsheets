from emailList import listOfEmails
from queryEmail import emailQuery

infile = ""
outfile = ""
emailListFile = ""

def main():
    emails = (listOfEmails(emailListFile))
    for email in emails:
        emailQuery(infile, outfile, email)

if __name__ == '__main__':
    main()