import moviepy.editor as mp
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract OCR\tesseract.exe'

def extract_Text_from_video():
    try:
        video_path = input('Enter your video path: ')
        video_clip = mp.VideoFileClip(video_path)
        n_frames = int(video_clip.fps * video_clip.duration)

        text_file = open(video_path.split('.')[0]+'.txt','x')

        for i in range(n_frames):
            frame = video_clip.get_frame(i)
            image = Image.fromarray(frame)
            text = tess.image_to_string(image)
            text_file.writelines(text.strip())

    except Exception as e:
        print(e)

extract_Text_from_video()