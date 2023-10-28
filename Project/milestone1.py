import yt_dlp

# Function to download video and its captions
def download_video_with_captions(video_url, output_directory):
    ydl_opts = {
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
        'writesubtitles': True,
        'subtitleslangs': ['en'],  # Download English captions
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Main function to download multiple videos from the playlist
def download_videos_from_playlist(playlist_url, output_directory, num_videos=10):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        playlist_items = info_dict['entries'][:num_videos]

        for item in playlist_items:
            video_url = item['url']
            download_video_with_captions(video_url, output_directory)

if __name__ == "__main__":
    # Specify the URL of the "60 Minutes" Interviews playlist
    playlist_url = "https://www.youtube.com/watch?v=h8PSWeRLGXs&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=7"
    
    # Specify the output directory where the videos and captions will be saved
    output_directory = "downloaded_videos"

    # Number of videos to download from the playlist
    num_videos_to_download = 10

    download_videos_from_playlist(playlist_url, output_directory, num_videos_to_download)
