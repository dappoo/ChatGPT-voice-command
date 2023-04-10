import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "your api token"
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source,duration=1)
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human","AI"]
    )
    return response.choices[0].text.strip()

def speak(text):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.say(text)
    engine.runAndWait()
while True:
    prompt = listen()
    response = generate_response(prompt)
    print("AI : " + response)
    speak(response)
