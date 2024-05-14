
import re
import requests
import smtplib
from email.mime.text import MIMEText


#Trouver tous les mails présents dans la page web
#[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
def find_mail(ch:str):
    regex_email = r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
    return re.findall(regex_email, ch)

#Récupérer le code source d'une page web se trouvant à l'URL passée en argument
def get_sourcecode(url:str):
    try: 
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            return html_content
        return None
    except Exception as e:
        print("Erreur:", e)
        return None

def parsing_webpage(url:str):
    return find_mail(get_sourcecode(url))

def main():
    print(parsing_webpage("https://www.oteria.fr"))
main()