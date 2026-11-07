#Pokretanje: python3 preslikavanja_stirling.py
from itertools import product, permutations
from math import comb, factorial


# Brojanje preslikavanja f: A -> B, |A| = k, |B| = n
def sva_preslikavanja(k, n):
    """Broj svih preslikavanja: n^k (nizovi duzine k nad n slova)."""
    return n ** k


def injektivna(k, n):
    """Broj injektivnih: n (n-1) ... (n-k+1) = n!/(n-k)!  (0 za k > n)."""
    r = 1
    for i in range(k):
        r *= n - i
    return r


# Stirlingovi brojevi druge vrste
def stirling_tablica(K):
    """S[k][n] = broj podela k-elementnog skupa na tacno n nepraznih blokova.
    Rekurencija: S(k, n) = n*S(k-1, n) + S(k-1, n-1), S(0,0)=1."""
    S = [[0] * (K + 1) for _ in range(K + 1)]
    S[0][0] = 1
    for k in range(1, K + 1):
        for n in range(1, k + 1):
            S[k][n] = n * S[k - 1][n] + S[k - 1][n - 1]
    return S


def na_preslikavanja(k, n, S):
    """Broj 'na' preslikavanja: n! * S(k, n)."""
    return factorial(n) * S[k][n] if k >= n else 0


def na_inkluzija_iskljucenje(k, n):
    """Isti broj preko formule: sum_i (-1)^i C(n,i) (n-i)^k."""
    return sum((-1) ** i * comb(n, i) * (n - i) ** k for i in range(n + 1))


# Provera grubom silom (nabrajanje svih funkcija)
def brute(k, n):
    sve = inj = na = 0
    for f in product(range(n), repeat=k): # f[i] = slika elementa i
        sve += 1
        if len(set(f)) == k:
            inj += 1
        if len(set(f)) == n:
            na += 1
    return sve, inj, na


def podele_skupa(elementi):
    """Generise sve podele skupa na neprazne blokove (za ispis primera)."""
    if not elementi:
        yield []
        return
    prvi, ostali = elementi[0], elementi[1:]
    for p in podele_skupa(ostali):
        yield [[prvi]] + p  # prvi je sam u bloku
        for i in range(len(p)): # ili ulazi u neki postojeci blok
            yield p[:i] + [[prvi] + p[i]] + p[i + 1:]


if __name__ == "__main__":
    K = 7
    S = stirling_tablica(K)

    print("Stirlingovi brojevi druge vrste S(k, n):")
    print("k\\n " + "".join(f"{n:5d}" for n in range(1, K + 1)))
    for k in range(1, K + 1):
        print(f"{k:3d} " + "".join(f"{S[k][n]:5d}" if n <= k else "     " for n in range(1, K + 1)))

    print("\nPodele skupa {1,2,3,4} na 2 bloka (ocekujemo S(4,2) = 7):")
    for p in podele_skupa([1, 2, 3, 4]):
        if len(p) == 2:
            print("  ", p)

    print("\nProvera grubom silom (svi / injektivna / na) i formule:")
    print(" k n | svi  inj  na | n^k  n!/(n-k)!  n!*S(k,n)  inkl-iskl")
    for k in range(1, 6):
        for n in range(1, 6):
            sve, inj, na = brute(k, n)
            f_na = na_preslikavanja(k, n, S) if k <= K else None
            assert sve == sva_preslikavanja(k, n)
            assert inj == injektivna(k, n) == (comb(n, k) * factorial(k) if k <= n else 0)
            assert na == f_na == na_inkluzija_iskljucenje(k, n)
            # n^k = sum_j C(n,j) * j! * S(k,j)   (klasifikacija po velicini slike)
            assert sve == sum(comb(n, j) * factorial(j) * S[k][j] for j in range(0, n + 1))
            print(f" {k} {n} | {sve:4d} {inj:4d} {na:3d} | {n**k:4d} {injektivna(k,n):9d} {na_preslikavanja(k,n,S):10d} {na_inkluzija_iskljucenje(k,n):9d}")
    print("\nSve provere prosle. OK")
    print("Primer: 4 razlicita zadatka na 3 osobe, svako dobija bar jedan:", na_preslikavanja(4, 3, S))
