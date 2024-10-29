import speech_recognition as sr
import re

def record_voice(time_limit=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio_data = recognizer.listen(source, phrase_time_limit=time_limit)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f'Your text: {text}')
        return text 
    except sr.UnknownValueError:
        print("Sorry, I don't understand")
    except sr.RequestError as e:
        print("Error, couldn't request result from Google Speech Recognition")
    return None

def speech_to_number(speech):
    numbers = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5
    }

    number = 0
    for word in speech.split():
        if word in numbers:
            number += numbers[word]
    return number

def calculator(text):
    number_speech = re.findall(r"\b(one|two|three|four|five)\b", text)
    operation = re.search(r"\b(add|subtract|multiply|divide)\b", text)

    numbers = [speech_to_number(number) for number in number_speech]

    if len(numbers) < 2:
        return "Error: Not enough numbers found"

    if operation:
        if operation.group() == "add":
            return numbers[0] + numbers[1]
        elif operation.group() == "subtract":
            return numbers[0] - numbers[1]
        elif operation.group() == "multiply":
            return numbers[0] * numbers[1]
        elif operation.group() == "divide":
            if numbers[1] != 0:
                return numbers[0] / numbers[1]
            else:
                return "Error: You cannot divide by 0"
    else:
        return "Operation error"

text = record_voice(time_limit=10)
if text:
    result = calculator(text)
    print(f"Result: {result}")
