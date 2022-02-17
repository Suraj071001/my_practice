import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

url = ('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=bc4a74c75ab149618017b773426da27b')
response = requests.get(url)
a = response.json()
print(response.json())
print(a["articles"][1])
for i in range(10) :
    if a["articles"][i]["title"] != None and a["articles"][i]["description"] != None :
        nt1 = a["articles"][i]["title"]
        nd1 = a["articles"][i]["description"]
        speak(nt1 + nd1)
    else :
        speak("sorry something wrong with this news,i can't tell you")