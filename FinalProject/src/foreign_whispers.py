# GROUP 3 - Zaid Abujumaiza and Maahir Vohra
from pytube import YouTube, extract
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import os
import whisper
from textblob import TextBlob
import pyttsx3

video_links = ["https://www.youtube.com/watch?v=OA2Tj75T3fI&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=4",
               "https://www.youtube.com/watch?v=mAFv55o47ok&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=31",
               "https://www.youtube.com/watch?v=oFVuQ0RP_As&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=6",
               "https://www.youtube.com/watch?v=4aPp8KX6EiU&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=7",
               "https://www.youtube.com/watch?v=h8PSWeRLGXs&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=8",
               "https://www.youtube.com/watch?v=Y9nM_9oBj2k&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=10",
               "https://www.youtube.com/watch?v=ervLwxz7xPo&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=11",
               "https://www.youtube.com/watch?v=Xw5dQBZavUw&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=19",
               "https://www.youtube.com/watch?v=C2M7j0UuMFY&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=24",
               "https://www.youtube.com/watch?v=bNKdlnoAqIs&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=28"]

if os.path.exists("audios") and os.path.exists("captions") and os.path.exists("audio-to-text") and os.path.exists("french-text") and os.path.exists("french-speech"):
    print("Audios and Captions already created!")
else:
    os.mkdir("audios")
    os.mkdir("captions")
    os.mkdir("audio-to-text")
    os.mkdir("french-text")
    os.mkdir("french-speech")

    model = whisper.load_model("base")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    for video_link in video_links:  
        video_id = extract.video_id(video_link)

        #get mp3 from youtube video and save in respective folder
        audio_file_name = f"audios/{video_id}.mp3"
        yt = YouTube(video_link)
        yt.streams.filter(only_audio=True).first().download(filename=audio_file_name)
        print("Created ", audio_file_name)

        #get captions from video and save in respective folder
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text_formatted = TextFormatter().format_transcript(transcript)
        text_file_name = f"captions/{video_id}.txt"
        with open(text_file_name, 'w', encoding='utf-8') as file:
            file.write(text_formatted)
        print("Created ", text_file_name)

        #get text from audio file and save in respective folder
        audio_to_text = model.transcribe(audio_file_name)["text"]
        audio_to_text_file_name = f"audio-to-text/{video_id}.txt"
        with open(audio_to_text_file_name, 'w', encoding='utf-8') as file:
            file.write(audio_to_text)
        print("Created ", audio_to_text_file_name)

        #translate audio text from english to french and save in respective folder
        french_text_file_name = f"french-text/{video_id}.txt"
        blob = TextBlob(audio_to_text)
        french_text = blob.translate(from_lang='en', to='fr')
        with open(french_text_file_name, 'w', encoding='utf-8') as file:
            file.write(str(french_text))
        print("Created ", french_text_file_name)

        #convert french text to audio using TTS
        french_speech_file_name = f"french-speech/{video_id}.mp3"
        engine.save_to_file(str(french_text), french_speech_file_name)
        engine.runAndWait()
        print("Created ", french_speech_file_name)
