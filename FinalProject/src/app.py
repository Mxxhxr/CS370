import PySimpleGUI as sg
from pytube import YouTube, extract
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import os
import whisper
from textblob import TextBlob
import pyttsx3

def download_and_process_video(url):
    video_id = extract.video_id(url)

    # Get mp3 from youtube video and save in respective folder
    audio_file_name = f"audios/{video_id}.mp3"
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(filename=audio_file_name)

    # Get captions from video and save in respective folder
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text_formatted = TextFormatter().format_transcript(transcript)
    text_file_name = f"captions/{video_id}.txt"
    with open(text_file_name, 'w', encoding='utf-8') as file:
        file.write(text_formatted)

    # Get text from audio file and save in respective folder
    audio_to_text = model.transcribe(audio_file_name)["text"]
    audio_to_text_file_name = f"audio-to-text/{video_id}.txt"
    with open(audio_to_text_file_name, 'w', encoding='utf-8') as file:
        file.write(audio_to_text)

    # Translate audio text from English to French and save in respective folder
    french_text_file_name = f"french-text/{video_id}.txt"
    blob = TextBlob(audio_to_text)
    french_text = blob.translate(from_lang='en', to='fr')
    with open(french_text_file_name, 'w', encoding='utf-8') as file:
        file.write(str(french_text))

    # Convert French text to audio using TTS
    french_speech_file_name = f"french-speech/{video_id}.mp3"
    engine.save_to_file(str(french_text), french_speech_file_name)
    engine.runAndWait()

    return text_file_name, french_text_file_name

layout = [
    [sg.Text("Enter YouTube URL:"), sg.InputText(key='-URL-')],
    [sg.Button("Download and Process"), sg.Button("Exit")],
    [sg.Text(size=(40, 1), key='-OUTPUT-')],
]

window = sg.Window("YouTube Video Processor", layout)

model = whisper.load_model("base")
engine = pyttsx3.init()
engine.setProperty('rate', 150)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Download and Process':
        url = values['-URL-']
        if url:
            try:
                original_captions, french_captions = download_and_process_video(url)
                window['-OUTPUT-'].update(f"Original Captions: {original_captions}\nFrench Captions: {french_captions}")
            except Exception as e:
                window['-OUTPUT-'].update(f"Error: {str(e)}")
        else:
            window['-OUTPUT-'].update("Please enter a valid YouTube URL.")

window.close()
