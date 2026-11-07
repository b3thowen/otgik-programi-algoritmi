# Pokretanje: python3 paskalov_trougao.py [N]

def paskalov_trougao(N):
    """Vraca listu redova Paskalovog trougla od reda 0 do reda N.
    c[n][m] = C(n, m); ivice su 1, a unutrasnji brojevi su zbir dva broja iznad."""
    c = []
    for n in range(N + 1):
        red = [1] * (n + 1)                      # c[n][0] = c[n][n] = 1
        for m in range(1, n):
            red[m] = c[n - 1][m - 1] + c[n - 1][m]   # Paskalov identitet
        c.append(red)
    return c


def ispisi(c):
    N = len(c) - 1
    w = len(str(max(c[-1]))) + 1                 # sirina jedne celije
    if w % 2:
        w += 1                                   # parna sirina da se red tacno centrira
    for n, red in enumerate(c):
        print(" " * ((N - n) * w // 2) + "".join(str(v).center(w) for v in red).rstrip())


if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    t = paskalov_trougao(N)
    ispisi(t)
    print()
    for n, red in enumerate(t):                  # provera: zbir reda je 2^n
        assert sum(red) == 2 ** n
        assert red == red[::-1]                  # simetrija
    print("Provera: zbir svakog reda je 2^n i svaki red je simetrican. OK")
