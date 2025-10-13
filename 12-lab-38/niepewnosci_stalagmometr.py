import numpy as np

# Dane pomiarowe
woda_mn = np.array([2.007, 2.038, 2.016])  # masa naczynia [g]
woda_mnw = np.array([3.452, 3.537, 3.519])  # masa naczynia z wodą [g]
alkohol_mn = np.array([1.997])  # masa naczynia [g]
alkohol_mnw = np.array([2.186])  # masa naczynia z alkoholem [g]

# Niepewności pomiarowe wagi
delta_m = 0.001  # g, niepewność pomiaru masy

# Gęstości (wartości tablicowe)
rho_woda = 0.9982  # g/cm³
rho_alkohol = 0.789  # g/cm³

# Obliczenie mas cieczy
m_woda = np.mean(woda_mnw - woda_mn)  # średnia masa 30 kropli wody
m_alkohol = np.mean(alkohol_mnw - alkohol_mn)  # średnia masa 30 kropli alkoholu

# Niepewność masy cieczy (suma niepewności dwóch pomiarów masy)
delta_m_cieczy = 2 * delta_m  # Niepewność różnicy mas = suma niepewności

# Masa pojedynczej kropli
m_woda_1 = m_woda / 30
m_alkohol_1 = m_alkohol / 30

# Niepewność masy pojedynczej kropli
delta_m_woda_1 = delta_m_cieczy / 30
delta_m_alkohol_1 = delta_m_cieczy / 30

# Obliczenie stosunku napięć powierzchniowych
sigma_ratio = (rho_alkohol * m_alkohol_1) / (rho_woda * m_woda_1)

# Prawo przenoszenia niepewności maksymalnych dla ilorazu:
# sigma_ratio = (rho_a * m_a) / (rho_w * m_w)
# Δ(sigma_ratio)/|sigma_ratio| = Δ(m_a)/|m_a| + Δ(m_w)/|m_w|

relative_uncertainty = delta_m_alkohol_1 / abs(m_alkohol_1) + delta_m_woda_1 / abs(
    m_woda_1
)

delta_sigma_ratio = sigma_ratio * relative_uncertainty

# Wartości referencyjne
sigma_ratio_ref = 0.3036  # stosunek tablicowy
relative_error = abs(sigma_ratio - sigma_ratio_ref) / sigma_ratio_ref * 100

print("\nWyniki dla metody stalagmometru:")
print(f"\nMasa 30 kropli:")
print(f"Woda: {m_woda:.4f} ± {delta_m_cieczy:.4f} g")
print(f"Alkohol: {m_alkohol:.4f} ± {delta_m_cieczy:.4f} g")

print(f"\nMasa pojedynczej kropli:")
print(f"Woda: {m_woda_1:.4f} ± {delta_m_woda_1:.4f} g")
print(f"Alkohol: {m_alkohol_1:.4f} ± {delta_m_alkohol_1:.4f} g")

print(f"\nStosunek napięć powierzchniowych (alkohol/woda):")
print(f"σ_a/σ_w = {sigma_ratio:.4f} ± {delta_sigma_ratio:.4f}")
print(f"Wartość tablicowa: {sigma_ratio_ref:.4f}")
print(f"Błąd względny: {relative_error:.1f}%")
