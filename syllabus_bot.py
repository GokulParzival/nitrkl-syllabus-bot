import requests


def syllabus_finder(s_code):
    url = "https://sheetdb.io/api/v1/q1qqa1kg7bit1"
    json_syllabus = requests.get(url).json()
    size = len(json_syllabus)
    print("URL working fine")
    for i in range(size):
        dictionary = json_syllabus[i]
        subject = dictionary["Code"]
        if subject == s_code:
            sub_name = dictionary["Subject Name"]
            syl = dictionary['Syllabus']
            books = dictionary["Books"]

    return sub_name, syl, books
