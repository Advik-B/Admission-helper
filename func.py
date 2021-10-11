import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject, sender_email, receiver_email, password, body, attachment=None):


    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = attachment  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

# Add attachment to message and convert message to string
    message.attach(part)
        
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

class Student():
    """Student:
    ---
    Args:
                    
        parent_email (str): email of the parent
        student_email (str): email of the student
        name (str): name
        sex (str): gender [male/female/other]
        age (float): age
        address (str): home address
        hobbies (list):  list of all the hobbies
        passport_size_photo (bytes): the display pic
        admission_number (int, optional): If any. Defaults to None.
        like_to_be_called_as (str, optional): Nick Name. Defaults to None.
        """
    def __init__(self,
                 parent_email:str,
                 student_email:str,
                 parent_name:list,
                 name:str,
                 sex:str,
                 age:float,
                 address:str,
                 hobbies:list,
                 blood_group:str,
                 parent_phone_number:int,
                 passport_size_photo:bytes,
                 admission_number:int=None,
                 like_to_be_called_as:str=None,
                 
                 ):
        """Student:
        ---

            Args:
                            
                parent_email (str): email of the parent
                student_email (str): email of the student
                name (str): name
                sex (str): gender [male/female/other]
                age (float): age
                address (str): home address
                hobbies (list):  list of all the hobbies
                passport_size_photo (bytes): the display pic
                admission_number (int, optional): If any. Defaults to None.
                like_to_be_called_as (str, optional): Nick Name. Defaults to None.
        """

        self.name = name
        self.email = student_email
        self.sex = sex
        self.contact_email = parent_email
        self.age = age
        self.address = address
        self.hobbies = hobbies
        self.admission_number = admission_number
        self.nickname = like_to_be_called_as
        self.photo = passport_size_photo
        self.parents = parent_name
        self.blood = blood_group
        self.parent_phone = parent_phone_number
        print(f'Student initialization completed.\nThe details are:\n\nname: {self.name}\nage:\
 {self.age}\nsex: {self.sex}\nnickname: {self.nickname}\nemail: {self.email}\n\nThere are some more details. use getinfo() method for the full list')
        
    def getinfo(self) -> dict:
        """Use this function to get all the information returned in a dictionary

        Returns:
            dict: consisting of all the variables
        """
        self.info_dict = {'name':self.name,
                     'age':self.age,
                     'sex':self.sex,
                     'address':self.address,
                     'email':self.email,
                     'parent-email':self.contact_email,
                     'nick':self.nickname,
                     'admission-number':self.admission_number,
                     'hobbies':self.hobbies,
                     'photo':self.photo,
                     'parents':self.parents
                     }
        return self.info_dict

    def send_accepted_mail(self, from_, to, password):
        self.school = 'KV AFS Begumpet'
        self.message = f"""\n
        Hello {str(self.parents).replace('[','').replace(']', '').replace("'", '')}
        
        We are pleased to inform you that your child ({self.name})
        has been accepted into the following school:
            {self.school}
        
        The full details are:
            student name: {self.name}
            student age: {self.age}
            student sex: {self.sex}
            student blood group: {self.blood}
            student email: {self.email}
            student hobbies: {str(self.hobbies).replace('[','').replace(']', '').replace("'", '')}
            student nickname: {self.nickname}
            student admission number: {self.admission_number} 
            student photo: (attached to email)
            parent phone number: {self.parent_phone}
            student address:
            {self.address}
        
        If the above information is incorrect, please contact the staff on premisis
        
        """
        with open('student.png', 'wb+') as pic:
            pic.write(self.photo)
        send_mail(
            
            subject=f'Admission for {self.name} accepted',
            attachment='student.png',
            receiver_email=to,
            sender_email=from_,
            password=password,
            body=self.message
        )
        
    def send_reject_mail(self, from_, to, password):
        
        self.school = 'KV AFS Begumpet'
        self.message = f"""\n
        Hello {str(self.parents).replace('[','').replace(']', '').replace("'", '')}
        
        We are sorry to inform you that your child ({self.name})
        has been rejected from the following school:
            {self.school}
        
        regards
        - Admission-bot
        """
        with open('student.png', 'wb+') as pic:
            pic.write(self.photo)
        send_mail(
            
            subject=f'Admission for {self.name} rejected',
            attachment='student.png',
            receiver_email=to,
            sender_email=from_,
            password=password,
            body=self.message
        )
    
    def send_ē_mail(self, from_, to, password):
        
        self.school = 'KV AFS Begumpet'
        self.message = f"""\n
        Hello {str(self.parents).replace('[','').replace(']', '').replace("'", '')}
        
        I am admission-bot made by Advik (https://github.com/Advik-B)
        
        Here are deatails of the registration:
        
            student name: {self.name}
            student age: {self.age}
            student sex: {self.sex}
            student blood group: {self.blood}
            student email: {self.email}
            student hobbies: {str(self.hobbies).replace('[','').replace(']', '').replace("'", '')}
            student nickname: {self.nickname}
            student admission number: {self.admission_number} 
            student photo: (attached to email)
            parent phone number: {self.parent_phone}
            student address:
            {self.address}
                
        If the above information is incorrect, you can correct it if you your ward gets accepted
                
        """
        with open('student.png', 'wb+') as pic:
            pic.write(self.photo)
        send_mail(
            
            subject=f'Admission for {self.name}',
            attachment='student.png',
            receiver_email=to,
            sender_email=from_,
            password=password,
            body=self.message
        )


with open('sample/1.jpg', 'rb') as a:
    stud = Student('par.email', 'stud.email', ['Keerti', 'Sirisha'], 'Advik Bommu', 'male', 14.8, '~', ['programming', 'minecraft'], 'A+', 9849653186, a.read(), 1232132, 'Advik')

stud.send_ē_mail(from_='admission.helper.app@gmail.com', to='advik.b@gmail.com', password='Dec@2612')
    