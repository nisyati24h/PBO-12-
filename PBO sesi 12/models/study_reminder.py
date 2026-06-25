from models.reminder_manager import Reminder

class StudyReminder(Reminder):
    def send_reminder(self):
        return "Saatnya Belajar!"