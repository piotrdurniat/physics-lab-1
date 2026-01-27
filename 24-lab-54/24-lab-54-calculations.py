import matplotlib.pyplot as plt
import numpy as np

C_known = np.array([1, 2, 3, 4.5, 5, 6.5, 7, 8, 9])

times_R1_raw = [
    "0:12,63",
    "0:25,62",
    "0:37,75",
    "0:58,0",
    "1:04,00",
    "1:23,84",
    "1:31,84",
    "1:44,03",
    "1:57,28",
]

times_R2_raw = [
    "0:23,32",
    "0:46,37",
    "1:09,15",
    "1:43,84",
    "1:50,07",
    "2:30,91",
    "2:43,43",
    "3:07,75",
    "3:30,66",
]

time_Cx_R1_raw = "0:45,65"
time_Cx_R2_raw = "1:29,22"

R1 = 1.4e6
R2 = 2.6e6
N_cycles = 20
u_T_inst = 0.01
u_C_inst = 0.05e-6


def parse_time(t_str):
    """Konwertuje czas z formatu 'mm:ss,ms' na sekundy (float)."""
    t_str = t_str.replace(",", ".")

    if ":" in t_str:
        parts = t_str.split(":")
        minutes = float(parts[0])
        seconds = float(parts[1])
        return minutes * 60 + seconds
    else:
        return float(t_str)


def calc_uncertainty_K(T, R, C, K_val):
    """Oblicza u(K) metodą różniczki zupełnej (propagacja błędu)."""
    term_T = (1 / (R * C)) * u_T_inst
    term_C = (-T / (R * C**2)) * u_C_inst
    return np.sqrt(term_T**2 + term_C**2)


def calc_uncertainty_Cx(Tx, R, K, Cx_val, u_K_val):
    """Oblicza u(Cx) metodą różniczki zupełnej."""
    term_Tx = (1 / (K * R)) * u_T_inst
    term_K = (-Tx / (K**2 * R)) * u_K_val
    return np.sqrt(term_Tx**2 + term_K**2)


C_F = C_known * 1e-6

times_R1 = np.array([parse_time(t) for t in times_R1_raw])
T_R1 = times_R1 / N_cycles
K_R1 = T_R1 / (R1 * C_F)

times_R2 = np.array([parse_time(t) for t in times_R2_raw])
T_R2 = times_R2 / N_cycles
K_R2 = T_R2 / (R2 * C_F)

K_mean_R1 = np.mean(K_R1)
K_mean_R2 = np.mean(K_R2)
K_mean_total = (K_mean_R1 + K_mean_R2) / 2

t_Cx_R1 = parse_time(time_Cx_R1_raw)
T_Cx_R1 = t_Cx_R1 / N_cycles
Cx_R1 = T_Cx_R1 / (K_mean_total * R1)

t_Cx_R2 = parse_time(time_Cx_R2_raw)
T_Cx_R2 = t_Cx_R2 / N_cycles
Cx_R2 = T_Cx_R2 / (K_mean_total * R2)

Cx_mean = (Cx_R1 + Cx_R2) / 2

# Oblicz niepewności dla wszystkich pomiarów K
u_K_R1 = np.array([calc_uncertainty_K(T_R1[i], R1, C_F[i], K_R1[i]) for i in range(len(K_R1))])
u_K_R2 = np.array([calc_uncertainty_K(T_R2[i], R2, C_F[i], K_R2[i]) for i in range(len(K_R2))])

# Średnia niepewność K (złożona z obu serii)
u_K_mean = np.sqrt(np.mean(u_K_R1**2) + np.mean(u_K_R2**2)) / 2

u_Cx_R1 = calc_uncertainty_Cx(T_Cx_R1, R1, K_mean_total, Cx_R1, u_K_mean)
u_Cx_R2 = calc_uncertainty_Cx(T_Cx_R2, R2, K_mean_total, Cx_R2, u_K_mean)

u_Cx_mean = 0.5 * np.sqrt(u_Cx_R1**2 + u_Cx_R2**2)

print("=" * 60)
print("     WYNIKI DO SPRAWOZDANIA (Exercise 54)")
print("=" * 60)

print(f"\n--- WYZNACZANIE STAŁEJ K ---")
print(f"K_sr (Seria I):  {K_mean_R1:.4f}")
print(f"K_sr (Seria II): {K_mean_R2:.4f}")
print(f"K_sr (Całość):   {K_mean_total:.4f}  <-- Do użycia w obliczeniach Cx")

print(f"\n--- WYZNACZANIE Cx ---")
print(f"Cx (z R=1.4M): {Cx_R1 * 1e6:.4f} uF")
print(f"Cx (z R=2.6M): {Cx_R2 * 1e6:.4f} uF")
print(f"Cx (Średnia):  {Cx_mean * 1e6:.4f} uF")

print(f"\n--- NIEPEWNOŚCI ---")
print(f"u(K) średnia (R=1.4M):        {np.mean(u_K_R1):.4f}")
print(f"u(K) średnia (R=2.6M):        {np.mean(u_K_R2):.4f}")
print(f"u(K) średnia całkowita:       {u_K_mean:.4f}")
print(f"u(Cx) (R=1.4M):               {u_Cx_R1 * 1e6:.4f} uF")
print(f"u(Cx) (R=2.6M):               {u_Cx_R2 * 1e6:.4f} uF")
print(f"u(Cx_mean) końcowe:            {u_Cx_mean * 1e6:.4f} uF")

print("\n" + "=" * 60)
print("     DANE DO TABEL (Kopiuj do LaTeX)")
print("=" * 60)

print("\n--- TABELA WYNIKÓW: Seria I (R=1.4 M) ---")
print(f"{'C [uF]':<8} | {'t20 [s]':<10} | {'T [s]':<10} | {'K':<10}")
print("-" * 46)
for i in range(len(C_known)):
    print(
        f"{C_known[i]:<8.1f} | {times_R1[i]:<10.2f} | {T_R1[i]:<10.4f} | {K_R1[i]:<10.4f}"
    )

print("\n--- TABELA WYNIKÓW: Seria II (R=2.6 M) ---")
print(f"{'C [uF]':<8} | {'t20 [s]':<10} | {'T [s]':<10} | {'K':<10}")
print("-" * 46)
for i in range(len(C_known)):
    print(
        f"{C_known[i]:<8.1f} | {times_R2[i]:<10.2f} | {T_R2[i]:<10.4f} | {K_R2[i]:<10.4f}"
    )

plt.figure(figsize=(10, 6))

plt.plot(C_known, T_R1, "bo", label=r"Pomiary R=1.4 M$\Omega$")
a1, b1 = np.polyfit(C_known, T_R1, 1)
plt.plot(C_known, a1 * C_known + b1, "b--", alpha=0.5, label=f"Regresja R1")

plt.plot(C_known, T_R2, "rs", label=r"Pomiary R=2.6 M$\Omega$")
a2, b2 = np.polyfit(C_known, T_R2, 1)
plt.plot(C_known, a2 * C_known + b2, "r--", alpha=0.5, label=f"Regresja R2")

# Odczytaj C_x z wykresów (z regresji liniowej)
# Z regresji: T = a*C + b, więc C = (T - b)/a
Cx_from_graph_R1 = (T_Cx_R1 - b1) / a1 if a1 != 0 else 0
Cx_from_graph_R2 = (T_Cx_R2 - b2) / a2 if a2 != 0 else 0
Cx_from_graph_mean = (Cx_from_graph_R1 + Cx_from_graph_R2) / 2

plt.scatter(
    np.array([Cx_R1 * 1e6]),
    np.array([T_Cx_R1]),
    color="cyan",
    zorder=5,
    edgecolors="black",
    s=100,
    label=rf"Cx1 (obl)={Cx_R1*1e6:.2f}$\mu$F",
)
plt.scatter(
    np.array([Cx_R2 * 1e6]),
    np.array([T_Cx_R2]),
    color="magenta",
    zorder=5,
    edgecolors="black",
    s=100,
    label=rf"Cx2 (obl)={Cx_R2*1e6:.2f}$\mu$F",
)

plt.title(r"Zależność okresu drgań relaksacyjnych od pojemności $T = f(C)$")
plt.xlabel(r"Pojemność C [$\mu$F]")
plt.ylabel("Okres T [s]")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()

output_filename = "report/img/wykres_TC_poprawiony.png"
plt.savefig(output_filename, dpi=300)
print(f"\n[INFO] Wykres zapisano jako '{output_filename}'")

print(f"\n--- PORÓWNANIE: OBLICZENIA VS WYKRES ---")
print(f"Cx z wykresu (R=1.4M): {Cx_from_graph_R1:.4f} uF")
print(f"Cx z wykresu (R=2.6M): {Cx_from_graph_R2:.4f} uF")
print(f"Cx z wykresu (Średnia): {Cx_from_graph_mean:.4f} uF")
print(f"Różnica |obl-wykres|: {abs(Cx_mean - Cx_from_graph_mean):.4f} uF")

print(f"\n[WYNIK KOŃCOWY]: Cx = ({Cx_mean * 1e6:.2f} +/- {u_Cx_mean * 1e6:.2f}) uF")

plt.show()
