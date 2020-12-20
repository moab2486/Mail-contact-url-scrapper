import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from flask import Flask, jsonify

email_regex = re.compile(r"[\w\.-]+@[\w\.-]+")
phone_num = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
url_https_regex = re.compile(r"https?://www\.?\w+\.\w+")
url_regex = re.compile(r"http?://www\.?\w+\.\w+")
app = Flask(__name__)

@app.route("/")
def hello():
    url = "https://bpe.gov.ng/about/"
    r = urlopen(url)  
    html = r.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    res = email_regex.findall(text)
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)