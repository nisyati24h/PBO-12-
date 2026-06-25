from models.reminder_manager import Reminder

class ScreenReminder(Reminder):
    def send_reminder(self):
        return "Screen Time Anda Sudah Melebihi Batas!"