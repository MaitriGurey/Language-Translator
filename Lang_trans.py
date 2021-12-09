from textblob import TextBlob
import speech_recognition as sr
recognizer = sr.Recognizer()

with sr.Microphone() as source: #recognizing voice from microphone
    print("Adjusting Noises...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("You want to speak in...")
    source_lang=input()
    print("How long you want to record (in seconds): ")
    time = int(input())
    print("Recording for ",time," seconds...")
    recorded_audio = recognizer.listen(source, timeout=time)
    print("Recording is done !")

    try:
        print("Recognizing the text from the recorded audio")
        text = str(recognizer.recognize_google(
            recorded_audio,language = source_lang #Converting speech to text 
        ))
        print("You spoke: {}".format(text))
        print("You want to translate in...")
        dest_lang=input()
        blob = TextBlob(text)
        output=blob.translate(to=dest_lang) #Translating to user input language
        print("You spoke: {}".format(output))

    except Exception as ex:
        print("Something went wrong...please speak again!")
        print(ex)
