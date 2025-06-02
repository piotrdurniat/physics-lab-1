import numpy as np
from uncertainties import ufloat, unumpy
from uncertainties.umath import sqrt

# Dane pomiarowe
woda_mn = np.array([2.007, 2.038, 2.016])  # masa naczynia [g]
woda_mnw = np.array([3.452, 3.537, 3.519])  # masa naczynia z wodą [g]
alkohol_mn = np.array([1.997])  # masa naczynia [g]
alkohol_mnw = np.array([2.186])  # masa naczynia z alkoholem [g]

# Obliczenie masy cieczy
woda_mw = woda_mnw - woda_mn
alkohol_mw = alkohol_mnw - alkohol_mn

# Obliczenie średnich wartości i niepewności dla wody
woda_mw_mean = np.mean(woda_mw)
woda_mw_std = np.std(woda_mw, ddof=1) / np.sqrt(len(woda_mw))  # niepewność typu A
woda_mw_unc_B = 0.001 / np.sqrt(3)  # niepewność typu B (dokładność wagi 0.001g)
woda_mw_unc = np.sqrt(woda_mw_std**2 + woda_mw_unc_B**2)

# Dla alkoholu mamy tylko jeden pomiar, więc bierzemy tylko niepewność typu B
alkohol_mw_mean = np.mean(alkohol_mw)
alkohol_mw_unc = woda_mw_unc_B

# Tworzenie obiektów ufloat dla wyników z niepewnościami
woda_result = ufloat(woda_mw_mean, woda_mw_unc)
alkohol_result = ufloat(alkohol_mw_mean, alkohol_mw_unc)

print("\nWyniki dla 30 kropli:")
print(f"Masa wody: {woda_result:.4f} g")
print(f"Masa alkoholu: {alkohol_result:.4f} g")

# Obliczenie masy pojedynczej kropli
print("\nMasa pojedynczej kropli:")
woda_kropla = woda_result / 30
alkohol_kropla = alkohol_result / 30
print(f"Woda: {woda_kropla:.4f} g")
print(f"Alkohol: {alkohol_kropla:.4f} g")

# Obliczenie stosunku mas kropli
stosunek = alkohol_kropla / woda_kropla
print(f"\nStosunek masy kropli alkoholu do wody: {stosunek:.4f}")

# Obliczenie stosunku napięć powierzchniowych
# σ1/σ2 = (ρ1*m1)/(ρ2*m2), gdzie ρ to gęstość, m to masa kropli
rho_woda = 0.9982  # g/cm³ w 20°C
rho_alkohol = 0.789  # g/cm³ w 20°C

sigma_ratio = (rho_alkohol * alkohol_kropla) / (rho_woda * woda_kropla)
print(f"\nStosunek napięć powierzchniowych (alkohol/woda): {sigma_ratio:.4f}")

# Porównanie z wartościami tablicowymi
sigma_woda_ref = 0.07280  # N/m
sigma_alkohol_ref = 0.02210  # N/m
sigma_ratio_ref = sigma_alkohol_ref / sigma_woda_ref

print(f"\nStosunek tablicowy napięć powierzchniowych: {sigma_ratio_ref:.4f}")
print(
    f"Błąd względny stosunku: {abs(sigma_ratio.n - sigma_ratio_ref)/sigma_ratio_ref*100:.1f}%"
)
