import threading
import time
from datetime import datetime

def set_alarm(alarm_time_str, callback=None):
    def alarm_task():
        while True:
            current_time = datetime.now().strftime("%H:%M")
            if current_time == alarm_time_str:
                print(f"⏰ Alarm triggered at {alarm_time_str}")
                if callback:
                    callback("Bot", f"Alarm ringing at {alarm_time_str}!")
                break
            time.sleep(30)

    threading.Thread(target=alarm_task).start()
    return f"✅ Alarm set for {alarm_time_str}"
