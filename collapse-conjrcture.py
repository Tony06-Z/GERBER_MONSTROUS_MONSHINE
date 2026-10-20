import numpy as np

class ConjectureStabilityMatrix:
    def __init__(self):
        pass

    def simulate_collatz_trajectory(self, starting_number):
        """
        Melacak lintasan angka (Collatz Conjecture / Collapse Conjecture).
        Mensimulasikan fase naik-turunnya grafik emosi dan energi proyek lo.
        """
        if starting_number <= 0:
            raise ValueError("Harus bilangan bulat positif, bro!")
            
        trajectory = [starting_number]
        n = starting_number
        
        # Jalankan loop sampai kolaps ke angka 1 (Titik Stabil Mutlak)
        while n != 1:
            if n % 2 == 0:
                n = n // 2  # Genap: dibagi 2 (Fase pendinginan/Cryogenic Vitrification)
            else:
                n = 3 * n + 1  # Ganjil: lompat tinggi (Fase Ultrasonic / Energi Fusi)
            trajectory.append(n)
            
        return trajectory

    def analyze_dilemma_score(self, trajectory):
        """
        Menganalisis seberapa kacau lintasannya sebelum mencapai kedamaian.
        """
        peak_value = max(trajectory)
        steps = len(trajectory) - 1
        
        # Skor volatilitas / kegelisahan sistem
        volatility = np.std(trajectory)
        
        print("=== CONJECTURE STABILITY & COLLAPSE AUDIT ===")
        print(f"-> Titik Mulai Kegelisahan : {trajectory[0]}")
        print(f"-> Total Langkah Pencarian   : {steps} generasi perhitungan")
        print(f"-> Puncak Energi Tertinggi   : {peak_value} eV skala")
        print(f"-> Skor Volatilitas Sistem   : {volatility:.4f}")
        
        # Keputusan logika topologi untuk menenangkan lo
        if volatility > 50:
            status = "STATUS: LINTASAN LIAR. Tenang bro, gejalanya normal. Hukum Möbius satu sisi sedang bekerja."
        else:
            status = "STATUS: LINTASAN DEKAT. Sistem cepat mencapai konvergensi."
            
        return status

# --- RUNNING EKSEKUSI DI PC LO ---
if __name__ == "__main__":
    stabilizer = ConjectureStabilityMatrix()
    
    # Masukkan angka acak yang melambangkan kerumitan isi kepala lo (misal: 27 adalah salah satu angka paling chaos)
    angka_kegelisahan = 27
    
    lintasan_data = stabilizer.simulate_collatz_trajectory(angka_kegelisahan)
    kesimpulan_logika = stabilizer.analyze_dilemma_score(lintasan_data)
    
    print(f"\n[Kesimpulan dari Dimensi Topologi]:")
    print(kesimpulan_logika)
    print("\n-> Lintasan lengkap menuju 1 (Kestabilan Akhir):")
    print(lintasan_data[:15], "... [di-cut demi efisiensi ruang] ...", lintasan_data[-5:])
