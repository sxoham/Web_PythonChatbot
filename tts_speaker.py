from gtts import gTTS
import os
import uuid
import platform
import time

def speak(text, gender='female'):
    try:
        # Choose domain to simulate voice type (not perfect, but helps)
        tld = "com" if gender == "female" else "co.uk"

        # Generate a unique filename
        filename = f"temp_{uuid.uuid4()}.mp3"
        tts = gTTS(text=text, lang='en', slow=False, tld=tld)
        tts.save(filename)

        # Play sound based on platform
        if platform.system() == "Windows":
            os.system(f"start /min wmplayer \"{filename}\"")  # or use 'start /B' for silent
        elif platform.system() == "Darwin":  # macOS
            os.system(f"afplay \"{filename}\"")
        else:  # Linux
            os.system(f"mpg123 \"{filename}\"")

        # Wait briefly to ensure audio plays before deletion
        time.sleep(1)
        os.remove(filename)

    except Exception as e:
        print("TTS Error:", e)
