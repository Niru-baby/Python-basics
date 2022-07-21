from cgitb import text
from typing import Concatenate
import PyPDF2
import re
import os
import glob

phone_pattern = r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})"
pattern = r"[a-zA-Z0-9.-_]+\.[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-_]+\.[a-zA-Z0-9.-_]+"
linkdin = r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+"
WED_DEV_SKILLS = [
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
    'web developer',
    'html',
    'css',
    'Project management',
    'Strong decision maker',
    'Complex problem solver',
]



def get_text_from_pdf(file_path):
    file_content = open(file_path, "rb")
    reader = PyPDF2.PdfReader(file_content)
    doc = ""
    pdf = glob.glob("*.pdf")
    # length=len(glob.glob("*.pdf"))
    # print(length)
    for page in range(reader.getNumPages()):
        p = reader.getPage(page)
        text_data = p.extractText()
        #print(text_data)
        doc+=text_data
    return doc

length=len(glob.glob("*.pdf"))  
for k in range(1, length//2):
    file_path = get_text_from_pdf(os.path.join(os.getcwd(), "New Folder","cv.pdf"))


def find_skills(text,file_path):
    skills = []
    for i in WED_DEV_SKILLS:
        pattern = re.compile(i)
        if bool(re.search(pattern, text.lower())):
            skills.append(i)
    return skills

text = get_text_from_pdf(os.path.join(os.getcwd(), "New Folder","cv.pdf" ))


email = re.findall(pattern,text)
phonenumber = re.findall(phone_pattern,text)
link_din = re.findall(linkdin,text)
skills = find_skills(text,WED_DEV_SKILLS)


print(email)
print(phonenumber)
print(link_din)
print(skills)
