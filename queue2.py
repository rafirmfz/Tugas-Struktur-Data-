from collections import deque 
class TaskManager:
    def __init__(self):
        self.tasks = deque()  

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self):
        if not self.is_empty():
            return self.tasks.popleft()  # Menghapus tugas dari depan
        else:
            return "Tidak ada tugas dalam antrian!"

    def add_urgent_task(self, task):
        self.tasks.appendleft(task)

    def display_tasks(self):
        print(list(self.tasks))  # Konversi deque ke list untuk tampilan yang lebih jelas

    def is_empty(self):
        return len(self.tasks) == 0

if __name__ == "__main__":
    tasks = TaskManager()
    # Tambah tugas
    tasks.add_task("Kerjakan laporan")
    tasks.add_task("Meeting dengan tim")
    tasks.add_urgent_task("Bug fix urgent")  # Tugas ini masuk ke depan antrian
    # Tampilkan antrian tugas
    print("Daftar Tugas:")
    tasks.display_tasks()  # Output: ['Bug fix urgent', 'Kerjakan laporan', 'Meeting dengan tim']
    # Proses tugas
    print("Tugas dikerjakan:", tasks.remove_task())  # Output: Bug fix urgent
    # Tampilkan antrian setelah pemrosesan
    print("Daftar Tugas setelah pemrosesan:")
    tasks.display_tasks()  # Output: ['Kerjakan laporan', 'Meeting dengan tim']
   