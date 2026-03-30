import heapq
class EmergencyQueue:
    def __init__(self):
        self.queue = []  

    def add_patient(self, name, priority):
        heapq.heappush(self.queue, (priority, name))

    def process_patient(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]  # Mengembalikan nama pasien
        else:
            return "Antrian kosong!"

    def display_queue(self):
        sorted_queue = sorted(self.queue)  # Sort berdasarkan prioritas
        print([patient[1] for patient in sorted_queue])  # Hanya menampilkan nama pasien

    def is_empty(self):
        return len(self.queue) == 0
    
if __name__ == "__main__":
    queue = EmergencyQueue()
    # Tambah pasien
    queue.add_patient("Andi", 2)  # Serius
    queue.add_patient("Budi", 1)  # Kritis
    queue.add_patient("Citra", 3)  # Ringan
    queue.add_patient("Dewi", 1)  # Kritis
    # Tampilkan antrian
    print("Antrian saat ini:")
    queue.display_queue()  # Output: ['Budi', 'Dewi', 'Andi', 'Citra']
    # Proses pasien
    print("Pasien diproses:", queue.process_patient())  # Output: Budi
    # Tampilkan antrian setelah pemrosesan
    print("Antrian setelah pemrosesan:")
    queue.display_queue()  # Output: ['Dewi', 'Andi', 'Citra']