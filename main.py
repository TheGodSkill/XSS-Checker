import requests
from bs4 import BeautifulSoup
from tkinter import *


def check_xss():

    url = url_field.get()


    res = requests.get(url)


    soup = BeautifulSoup(res.content, "html.parser")


    input_tags = soup.find_all("input")
    script_tags = soup.find_all("script")


    test_payloads = ['<script>alert("XSS vulnerability test")</script>',
                     '"><script>alert("XSS vulnerability test")</script>']


    vulnerable_inputs = []
    vulnerable_scripts = []


    for input_tag in input_tags:
        if 'name' in input_tag.attrs:
            for payload in test_payloads:

                test_input_tag = input_tag
                test_input_tag['value'] = payload


                test_url = url + "?" + test_input_tag.attrs['name'] + "=" + test_input_tag.attrs['value']
                test_res = requests.get(test_url)


                if payload in test_res.text:
                    vulnerable_inputs.append(test_input_tag)


    for script_tag in script_tags:
        for payload in test_payloads:

            test_script_tag = script_tag
            test_script_tag.string = payload


            test_html = str(soup)
            test_html = test_html.replace(str(script_tag), str(test_script_tag))
            test_res = requests.get(url, params=test_html)


            if payload in test_res.text:
                vulnerable_scripts.append(test_script_tag)


    if not vulnerable_inputs and not vulnerable_scripts:
        result_label.config(text="The website is not vulnerable to XSS attacks")
    else:
        result_label.config(text="The website is vulnerable to XSS attacks")


        if vulnerable_inputs:
            input_label.config(text="Vulnerable input fields:")
            for input_tag in vulnerable_inputs:
                input_result_label = Label(root, text=f"Name: {input_tag.attrs['name']}, Value: {input_tag.attrs['value']}")
                input_result_label.pack()


        if vulnerable_scripts:
            script_label.config(text="Vulnerable script tags:")
            for script_tag in vulnerable_scripts:
                script_result_label = Label(root, text=script_tag.string)
                script_result_label.pack()


root = Tk()
root.title("XSS Vulnerability Checker")
root.geometry("600x400")

url_label = Label(root, text="Enter website URL:")
url_label.pack()

url_field = Entry(root)
url_field.pack()

check_button = Button(root, text="Check", command=check_xss)
check_button.pack()

result_label = Label(root, text="")
result_label.pack()

input_label = Label(root, text="")
input_label.pack()

script_label = Label(root, text="")

root.mainloop()