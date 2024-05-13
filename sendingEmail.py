import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from email.mime.base import MIMEBase
from email import encoders

def send_email(email_expediteur, mot_de_passe, email_destinataire,serveur_smtp="smtp.gmail.com", port=587):
  try:
    L=[('sujet 1', 'texte du mail 1'),('sujet 2','texte du mail 2'),('sujet 3', 'texte du mail 3') ]

    # Stockage des éléments du tuple dans des variables distinctes
    random_tuple = random.choice(L)
    sujet, corps = random_tuple
    
    # Création de l'objet message
    message = MIMEMultipart()
    message['From'] = email_expediteur
    message['To'] = email_destinataire
    message['Subject'] = "DOUCEUR"

    # Ajout du corps de l'email
    message.attach(MIMEText(corps, 'plain'))
    # Ajouter la pièce jointe
    filename = 'cute.jpg'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    message.attach(part)
    # Connexion au serveur et envoi de l'email
    with smtplib.SMTP(serveur_smtp, port) as server:
        server.starttls()  # Activation de la sécurité
        server.login(email_expediteur, mot_de_passe)
        text = message.as_string()
        server.sendmail(email_expediteur, email_destinataire, text)
    print("mail envoyé")
  except smtplib.SMTPServerDisconnected:
      print("La connexion au serveur SMTP a été fermée de manière inattendue.")
  except smtplib.SMTPException as e:
      print("Erreur SMTP : ", e)
  except Exception as e:
      print("Une erreur est survenue : ", e)
      
# Exemple d'utilisation
email_expediteur = 'younes3046@gmail.com'
mot_de_passe = 'jpyc irod qrfp gusc'
email_destinataire = 'younes.talbi@oteria.fr'

send_email(email_expediteur,mot_de_passe,email_destinataire)