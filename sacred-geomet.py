import numpy as np

def generate_sacred_horizon_layers(num_layers=5, base_radius=1.0):
    """
    Membuat lapisan mesh perbatasan event horizon menggunakan 
    prinsip ekspansi Golden Ratio (Phi) agar transisi ruang mulus.
    """
    phi = 1.61803398875 # Rasio Emas (Golden Ratio)
    layer_radii = []
    
    current_radius = base_radius
    for i in range(num_layers):
        # Setiap lapisan keluar mengembang secara proporsional suci
        layer_radii.append(current_radius)
        current_radius *= phi
        
    return np.array(layer_radii)

# Eksekusi pemetaan lapisan ruang horizon
radii_mesh = generate_sacred_horizon_layers(num_layers=6, base_radius=0.1)
print("Titik Jari-jari Lapisan Mesh Berbasis Golden Ratio:")
for idx, r in enumerate(radii_mesh):
    print(f"  Lapisan {idx + 1}: {r:.4f} meter")