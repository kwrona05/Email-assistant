import speech_recognition as sr

def record_voice(time_limit=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio_data = recognizer.listen(source, phrase_time_limit=time_limit)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f'Your text: {text}')
    except sr.UnknownValueError:
        print("Sorry, I don't understand")
    except sr.RequestError as e:
        print("Error, couldn't request result from Google Speech Recognition")
    
record_voice(time_limit=5)
