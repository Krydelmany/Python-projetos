import speech_recognition as sr
import subprocess

def recognize_speech(language='pt-BR'):
    # Inicia o reconhecedor de voz
    recognizer = sr.Recognizer()
    # Define o microfone como entrada
    with sr.Microphone() as source:
        # Diz ao reconhecedor para ouvir por 3 segundos
        recognizer.adjust_for_ambient_noise(source, duration=3)
        # Pede ao usuário para falar
        print("Diga alguma coisa")
        # Tenta reconhecer a fala
        audio = recognizer.listen(source)
        # Tenta converter a fala em texto
        try:
            text = recognizer.recognize_google(audio, language=language)
            print("Você disse:", text)
            return text  # Return the recognized text
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
            return None
        except sr.RequestError as e:
            print("Falha na requisição do Google Speech Recognition:", e)
            return None

if __name__ == "__main__":
    # Chama a função de reconhecimento de fala and store the recognized text in a variable
    recognized_text = recognize_speech()

    # Verifica se o usuário disse "abra o Firefox"
    if recognized_text == "Abra o spotify":
        subprocess.Popen(["spotify"])
    else:
        print("Não foi possivel abrir o spotify")

    if recognized_text == "abra o navegador":
        # Abre o edge
        subprocess.Popen(["microsoft-edge"])
