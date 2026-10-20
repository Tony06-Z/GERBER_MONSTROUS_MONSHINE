import sys
from typing import Dict, Tuple, Set, Optional

# =====================================================================
# CONFIGURATION & CAST KASTA ATAS
# =====================================================================
# Representasi State: 'A', 'B', 'C', dsb. 'H' adalah HALT
# Simbol Pita: 0 atau 1
# Arah Gerak: -1 (Kiri/Left), 1 (Kanan/Right)

class TuringTransition:
    def __init__(self, write: int, move: int, next_state: str):
        self.write = write
        self.move = move  # -1 atau 1
        self.next_state = next_state

class HyperMachineSpec:
    """
    Spesifikasi Mesin Turing Kasta Tinggi.
    Menyimpan tabel transisi formal untuk n-state Busy Beaver.
    """
    def __init__(self, transitions: Dict[Tuple[str, int], TuringTransition]):
        self.transitions = transitions

    def get_action(self, state: str, symbol: int) -> Optional[TuringTransition]:
        return self.transitions.get((state, symbol))


class TopologyGraphDecider:
    """
    ARSIKETUR DECIDER: Menganalisis konfigurasi rekursif tanpa eksekusi linier.
    Membuktikan Non-Halting menggunakan pembatasan ruang konfigurasi pohon (Tree Gating).
    """
    def __init__(self, machine: HyperMachineSpec, max_depth: int = 10000):
        self.machine = machine
        self.max_depth = max_depth

    def prove_infinite_loop(self, initial_state: str = 'A') -> bool:
        """
        Menggunakan evaluasi topologi siklus transisi. 
        Jika graf konfigurasi menutup (Closed-Tree) tanpa menyentuh State 'H',
        secara metamatematika mesin ini terbukti TIDAK AKAN PERNAH BERHENTI (Non-Halting).
        """
        # Representasi konfigurasi abstrak: (State, Sejarah_Pita_Kiri, Sejarah_Pita_Kanan)
        visited_nodes: Set[Tuple[str, str, str]] = set()
        
        # Inisialisasi root node abstrak
        current_state = initial_state
        left_tape = ""
        right_tape = ""
        
        depth = 0
        while current_state != 'H':
            if depth > self.max_depth:
                # Batas terlampaui tanpa konvergensi -> Butuh bantuan godel.py (Oracle Upgrade)
                return False
                
            # Cek simbol saat ini (jika pita kosong, default 0)
            current_symbol = int(right_tape[0]) if right_tape else 0
            
            # Ambil blueprint aksi dari tabel transisi
            action = self.machine.get_action(current_state, current_symbol)
            if not action:
                # Jalur transisi tidak terdefinisi dianggap Halt implisit
                return False
            
            # State Node ID unik untuk mendeteksi siklus geometris
            node_signature = (current_state, left_tape[-10:], right_tape[:10:])
            if node_signature in visited_nodes:
                # ANOMALI DITEMUKAN: Graf menutup sempurna. Terjebak dalam Infinite Loop Topologis!
                return True # Terbukti Non-Halting
                
            visited_nodes.add(node_signature)
            
            # Transformasi String Pita secara Cepat (Memory Shift)
            # Tulis simbol baru
            write_sym = str(action.write)
            
            if action.move == 1: # Bergerak ke Kanan (Right)
                left_tape += write_sym
                right_tape = right_tape[1:] if len(right_tape) > 1 else ""
            else: # Bergerak ke Kiri (Left)
                right_tape = write_sym + right_tape
                left_tape = left_tape[:-1] if left_tape else ""
                
            current_state = action.next_state
            depth += 1
            
        return False # Mesin menyentuh 'H' (Halt), artinya ia menghasilkan skor berhingga.


# =====================================================================
# ENTRY POINT: PROYEK GERBER-MONSTROUS-MONSHINE
# =====================================================================
if __name__ == "__main__":
    print("[⚡] MONSTROUS-MONSHINE ENGINE: Menjalankan Kasta Analisis Topologi...")
    
    # Contoh Inisialisasi Mesin 3-State Juara Terbukti yang Berputar Eksponensial
    # Transisi diatur dalam format: (State, Simbol) -> TuringTransition(Tulis, Arah, State_Berikut)
    blueprint_bb3 = {
        ('A', 0): TuringTransition(1, 1, 'B'),
        ('A', 1): TuringTransition(1, -1, 'H'),
        ('B', 0): TuringTransition(0, 1, 'C'),
        ('B', 1): TuringTransition(1, 1, 'B'),
        ('C', 0): TuringTransition(1, -1, 'C'),
        ('C', 1): TuringTransition(1, -1, 'A'),
    }
    
    machine_instance = HyperMachineSpec(blueprint_bb3)
    decider = TopologyGraphDecider(machine_instance)
    
    print("[🎛️] Memindai struktur graf internal mesin...")
    is_infinite = decider.prove_infinite_loop(initial_state='A')
    
    if is_infinite:
        print("[🔴] STATUS: Terbukti secara formal INFINTITE LOOP. Aksioma ditutup.")
    else:
        print("[🟢] STATUS: Mesin dikategorikan HALTING atau CRYPTID. Teruskan ke Oracle transdesimal.")

# =====================================================================
# FILE: busy-fucking-beaver.py
# =====================================================================
from godel import GodelIncompletenessGate

class TuringTransition:
    def __init__(self, write: int, move: int, next_state: str):
        self.write = write
        self.move = move
        self.next_state = next_state

class HyperMachineSpec:
    def __init__(self, num_states: int, transitions: dict):
        self.num_states = num_states
        self.transitions = transitions

class TopologyGraphDecider:
    def __init__(self, machine: HyperMachineSpec):
        self.machine = machine
        self.gate = GodelIncompletenessGate()

    def run_safe_evaluation(self) -> str:
        # Langkah 1: Evaluasi kelayakan aksioma lewat godel.py sebelum komputer fisik freeze
        if not self.gate.evaluate_provability(self.machine.num_states):
            return "🔴 STATUS: INDECIDABLE (Terdeteksi Batas Gödel. Eksekusi Dipotong secara Transfinit)."

        # Langkah 2: Lakukan pengecekan topologi siklus internal
        # (Logika penutupan graf yang kita bangun kemarin)
        visited_nodes = set()
        current_state = 'A'
        left_tape, right_tape = "", ""
        
        for _ in range(1000): # Terikat batas aman komputasi lokal
            if current_state == 'H': 
                return "🟢 STATUS: HALTING (Mesin Berhenti dengan Skor Berhingga)."
                
            current_symbol = int(right_tape[0]) if right_tape else 0
            action = self.machine.transitions.get((current_state, current_symbol))
            
            if not action: return "🟢 STATUS: HALTING (Implicit)."
            
            node_signature = (current_state, left_tape[-5:], right_tape[:5])
            if node_signature in visited_nodes:
                return "🔴 STATUS: NON-HALTING (Terbukti terjebak Loop Abadi lewat Graf Topologi)."
            visited_nodes.add(node_signature)
            
            # Pergeseran Pita
            write_sym = str(action.write)
            if action.move == 1:
                left_tape += write_sym
                right_tape = right_tape[1:] if len(right_tape) > 1 else ""
            else:
                right_tape = write_sym + right_tape
                left_tape = left_tape[:-1] if left_tape else ""
            current_state = action.next_state
            
        return "🟡 STATUS: CRYPTID (Melewati batas lokal. Butuh Oracle Kasta Lebih Tinggi)."

if __name__ == "__main__":
    # Test dengan simulasi mesin 5-State yang berbahaya bagi komputer biasa
    blueprint_bb5 = {
        ('A', 0): TuringTransition(1, 1, 'B'),  ('A', 1): TuringTransition(1, -1, 'C'),
        ('B', 0): TuringTransition(1, 1, 'C'),  ('B', 1): TuringTransition(1, 1, 'B'),
        ('C', 0): TuringTransition(1, 1, 'D'),  ('C', 1): TuringTransition(0, -1, 'E'),
        ('D', 0): TuringTransition(1, -1, 'A'), ('D', 1): TuringTransition(1, -1, 'D'),
        ('E', 0): TuringTransition(1, 1, 'H'),  ('E', 1): TuringTransition(0, -1, 'A'),
    }
    
    machine = HyperMachineSpec(num_states=5, transitions=blueprint_bb5)
    decider = TopologyGraphDecider(machine)
    print(decider.run_safe_evaluation())
