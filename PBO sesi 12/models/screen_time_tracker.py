class ScreenTimeTracker:

    def __init__(self):
        self.records = []

    def add_record(self, date, hours):

        self.records.append({
            "date": date,
            "hours": int(hours)
        })

    def get_records(self):
        return self.records

    def get_total_time(self):

        total = 0

        for record in self.records:
            total += record["hours"]

        return total