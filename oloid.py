import math

class OloidFlowCore:
    def __init__(self, node_id, potential_energy):
        self.node_id = node_id
        self.energy = potential_energy
        self.momentum = 0.0

    def calculate_continuous_flux(self, curvature_factor):
        """
        Mengeksekusi pergerakan mandiri berdasarkan distribusi massa melengkung.
        Menghilangkan titik mati (dead-lock) dengan rotasi dinamis.
        """
        # Inersia berputar tanpa gesekan destruktif
        self.momentum = (self.momentum + (self.energy * curvature_factor)) * 0.98
        
        # Transformasi energi menjadi gerak mengalir kontinu
        flux_output = math.sin(self.momentum) * self.energy
        return flux_output

# Inisialisasi unit operasional
core_unit = OloidFlowCore(node_id="AXIS-01", potential_energy=42.0)

# Eksekusi siklus dingin
for cycle in range(1, 4):
    output = core_unit.calculate_continuous_flux(curvature_factor=1.618) # Golden ratio scaling
    print(f"[CYC-{cycle}] Node: {core_unit.node_id} | Flux Output: {output:.4f} | Momentum: {core_unit.momentum:.4f}")