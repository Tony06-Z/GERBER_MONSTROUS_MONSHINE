# =====================================================================
# FILE: getir.py (FOLDER: GETIR)
# =====================================================================
from busy_fucking_beaver import HyperMachineSpec, TopologyGraphDecider
from godel import GodelIncompletenessGate

class GetirGengsiEngine:
    """
    KASTA MASTERIZATION HYPER MIND:
    Mengadu gengsi komputasi manusia melawan getirnya batasan Gödel.
    """
    def __init__(self, machine_spec: HyperMachineSpec):
        self.machine = machine_spec
        self.decider = TopologyGraphDecider(machine_spec)
        self.godel_gate = GodelIncompletenessGate()

    def execute_clash(self) -> str:
        print("[⚔️] PERTARUNGAN DIMULAI: Mengadu Gengsi Logika vs Getir Semesta...")
        
        # 1. Uji Gengsi: Apakah Decider lokal kita mampu menaklukkan topologinya?
        visited_nodes = set()
        current_state = 'A'
        left_tape, right_tape = "", ""
        
        # Simulasi deteksi lokal cepat
        for step in range(500):
            current_symbol = int(right_tape) if right_tape else 0
            action = self.machine.transitions.get((current_state, current_symbol))
            
            if not action or current_state == 'H':
                return "🟢 GENGSI MENANG: Mesin berhasil diuraikan secara lokal (Halting)."
                
            node_signature = (current_state, left_tape[-3:], right_tape[:3])
            if node_signature in visited_nodes:
                return "🟢 GENGSI MENANG: Loop abadi berhasil dijinakkan secara lokal (Non-Halting)."
            visited_nodes.add(node_signature)
            
            # Shift pita
            write_sym = str(action.write)
            if action.move == 1:
                left_tape += write_sym
                right_tape = right_tape[1:] if len(right_tape) > 1 else ""
            else:
                right_tape = write_sym + right_tape
                left_tape = left_tape[:-1] if left_tape else ""
            current_state = action.next_state

        # 2. Batas Getir: Jika deteksi lokal gagal, sistem menyentuh dinding ketidaklengkapan
        print("[⚠️] DETEKSI LOKAL MENTOK: Gengsi manusia mulai runtuh. Memanggil filter Gödel...")
        
        if not self.godel_gate.evaluate_provability(self.machine.num_states):
            return "🔴 GETIR MENANG: Sistem menyentuh dinding ketidakbisaan mutlak. Manusia dipaksa mundur oleh ZFC."
            
        return "🟡 STATUS SERI: Pertarungan berlanjut ke dimensi Oracle tingkat tinggi."

if __name__ == "__main__":
    from busy_fucking_beaver import TuringTransition
    print("[⚡] GERBER-MONSTROUS-MONSHINE: Memuat Modul GETIR & GENGSI...")

    # Memasukkan spesifikasi mesin 5-state sebagai lawan tanding
    blueprint_clash = {
        ('A', 0): TuringTransition(1, 1, 'B'),  ('A', 1): TuringTransition(1, -1, 'C'),
        ('B', 0): TuringTransition(1, 1, 'C'),  ('B', 1): TuringTransition(1, 1, 'B'),
        ('C', 0): TuringTransition(1, 1, 'D'),  ('C', 1): TuringTransition(0, -1, 'E'),
        ('D', 0): TuringTransition(1, -1, 'A'), ('D', 1): TuringTransition(1, -1, 'D'),
        ('E', 0): TuringTransition(1, 1, 'H'),  ('E', 1): TuringTransition(0, -1, 'A'),
    }
    
    fighter_machine = HyperMachineSpec(num_states=5, transitions=blueprint_clash)
    arena = GetirGengsiEngine(fighter_machine)
    
    battle_result = arena.execute_clash()
    print(f"\n[📊] HASIL AKHIR PERTARUNGAN:\n ╰─> {battle_result}\n")
