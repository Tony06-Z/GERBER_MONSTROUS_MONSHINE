# =====================================================================
# FILE: ablation.py
# =====================================================================
from typing import Dict, List, Tuple
from busy_fucking_beaver import HyperMachineSpec, TopologyGraphDecider

class AxiomaticAblationEngine:
    """
    KASTA MASTERIZATION HYPER MIND:
    Melakukan amputasi formal pada tabel transisi mesin dan sistem aksioma
    untuk menganalisis batas runtuhnya (collapse point) pembuktian Busy Beaver.
    """
    def __init__(self, target_machine: HyperMachineSpec):
        self.original_machine = target_machine
        self.ablation_history: List[str] = []

    def perform_transition_ablation(self, state_to_amputate: str, symbol_to_amputate: int) -> HyperMachineSpec:
        """
        Mengamputasi satu jalur transisi spesifik dari mesin Turing.
        Ini menyimulasikan hilangnya 'kapasitas memori logika' pada sistem formal.
        """
        mutated_transitions = self.original_machine.transitions.copy()
        target_key = (state_to_amputate, symbol_to_amputate)
        
        if target_key in mutated_transitions:
            del mutated_transitions[target_key]
            label = f"Amputasi Transisi: State {state_to_amputate} pada Simbol {symbol_to_amputate}"
            self.ablation_history.append(label)
            print(f"[✂️] ABLASI: {label} berhasil dieksekusi.")
        else:
            print(f"[⚠️] WARNING: Jalur {target_key} tidak ditemukan. Sistem stabil.")
            
        return HyperMachineSpec(num_states=self.original_machine.num_states, transitions=mutated_transitions)

    def run_ablation_stress_test(self) -> Dict[str, str]:
        """
        Secara sistematis memotong setiap sirkuit logika mesin untuk memetakan
        di titik mana mesin bertransformasi dari CRYPTID/NON-HALTING menjadi HALTING.
        """
        print("\n[🧬] Memulai Stress Test Ablasi pada Struktur Semesta Mesin...")
        report: Dict[str, str] = {}
        
        # Mengevaluasi semua kunci transisi yang ada saat ini
        keys_to_test = list(self.original_machine.transitions.keys())
        
        for state, symbol in keys_to_test:
            # Jalankan ablasi lokal
            ablated_machine = self.perform_transition_ablation(state, symbol)
            
            # Uji menggunakan Decider Topologi Graf yang terhubung dengan godel.py
            decider = TopologyGraphDecider(ablated_machine)
            result = decider.run_safe_evaluation()
            
            node_label = f"Ablated_({state},{symbol})"
            report[node_label] = result
            
        return report

# =====================================================================
# INTEGRASI KE ENGINE GERBER-MONSTROUS-MONSHINE
# =====================================================================
if __name__ == "__main__":
    from busy_fucking_beaver import TuringTransition
    print("[⚡] MONSTROUS-MONSHINE: Mengaktifkan Arsitektur Ablasi Aksioma...")

    # Kita ambil blueprint BB5 dari file utama sebagai subjek bedah
    blueprint_bb5 = {
        ('A', 0): TuringTransition(1, 1, 'B'),  ('A', 1): TuringTransition(1, -1, 'C'),
        ('B', 0): TuringTransition(1, 1, 'C'),  ('B', 1): TuringTransition(1, 1, 'B'),
        ('C', 0): TuringTransition(1, 1, 'D'),  ('C', 1): TuringTransition(0, -1, 'E'),
        ('D', 0): TuringTransition(1, -1, 'A'), ('D', 1): TuringTransition(1, -1, 'D'),
        ('E', 0): TuringTransition(1, 1, 'H'),  ('E', 1): TuringTransition(0, -1, 'A'),
    }
    
    base_machine = HyperMachineSpec(num_states=5, transitions=blueprint_bb5)
    
    # Inisialisasi pisau bedah ablasi
    surgeon = AxiomaticAblationEngine(base_machine)
    
    # Jalankan stress test untuk memetakan keruntuhan topologi
    ablation_report = surgeon.run_ablation_stress_test()
    
    print("\n[📊] HASIL DIAGNOSIS ABLASI TOPOLOGI:")
    for mutation, status in ablation_report.items():
        print(f" ╰─> Mutasi {mutation} => {status}")
