import numpy as np
import matplotlib.pyplot as plt

# Ustawienia estetyczne wykresów
plt.style.use('seaborn-v0_8-muted')
plt.rcParams['figure.figsize'] = (12, 7)

def simulate_gbm(S0, mu, sigma, T, dt, n_paths):
    """
    Symulacja Geometrycznego Ruchu Browna.
    S0 - cena początkowa
    mu - dryf (oczekiwana stopa zwrotu)
    sigma - zmienność
    T - czas (np. 1 rok)
    dt - krok czasowy (np. 1/252 dla dni giełdowych)
    n_paths - liczba symulowanych ścieżek
    """
    n_steps = int(T / dt)
    time = np.linspace(0, T, n_steps)
    
    # Generowanie przyrostów procesu Wienera (szum biały)
    # Wykorzystujemy wektoryzację zamiast pętli for
    Z = np.random.standard_normal((n_steps, n_paths))
    dW = Z * np.sqrt(dt)
    W = np.cumsum(dW, axis=0)
    
    # Rozwiązanie analityczne równania SDE
    # S_t = S_0 * exp((mu - 0.5 * sigma^2) * t + sigma * W_t)
    drift = (mu - 0.5 * sigma**2) * time.reshape(-1, 1)
    diffusion = sigma * W
    
    S = S0 * np.exp(drift + diffusion)
    
    return time, S

# Parametry symulacji
S0 = 100      # Cena początkowa
mu = 0.05     # 5% rocznego zwrotu
sigma = 0.25  # 25% zmienności
T = 1.0       # Horyzont 1 roku
dt = 1/252    # Krok jednodniowy
n_paths = 50  # Ścieżki do wizualizacji

# Obliczenia
t, prices = simulate_gbm(S0, mu, sigma, T, dt, n_paths)

# Wizualizacja
fig, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]}, sharey=True)

# Lewy wykres: Ścieżki cenowe
ax1.plot(t, prices, lw=0.8, alpha=0.6)
ax1.plot(t, prices.mean(axis=1), color='black', lw=2, label='Średnia (E[S_t])')
ax1.set_title(f'Symulacja Monte Carlo: Geometryczny Ruch Browna\n'
              rf'$\mu={mu}, \sigma={sigma}, S_0={S0}$', fontsize=14)
ax1.set_xlabel('Czas (lata)')
ax1.set_ylabel('Cena aktywa')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Prawy wykres: Rozkład końcowy
final_prices = prices[-1, :]
ax2.hist(final_prices, bins=30, orientation='horizontal', color='royalblue', alpha=0.7)
ax2.set_title('Rozkład cen końcowych')
ax2.set_xlabel('Częstość')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()