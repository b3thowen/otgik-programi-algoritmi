# Zadatak 5 - racunanje clanova niza po rekurentnoj relaciji
# a[n] = c[1]*a[n-1] + ... + c[k]*a[n-k] + f(n)

def niz_iteracijom(k, c, a, N, f=lambda n: 0):
    """c[1..k] su koeficijenti (c[0] se ne koristi), a[0..k-1] su pocetni uslovi.
    Vraca listu a[0..N]."""
    a = list(a)
    for n in range(k, N + 1):
        s = f(n)
        for i in range(1, k + 1):
            s += c[i] * a[n - i]
        a.append(s)
    return a


if __name__ == "__main__":
    # Fibonacijev niz: f(n) = f(n-1) + f(n-2), f(0) = 0, f(1) = 1
    fib = niz_iteracijom(2, [0, 1, 1], [0, 1], 10)
    print("Fibonacijev niz:", fib)
    assert fib == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # Hanojske kule: h(n) = 2h(n-1) + 1, h(1) = 1 (pocinjemo od h(0) = 0)
    h = niz_iteracijom(1, [0, 2], [0], 10, lambda n: 1)
    print("Hanojske kule:", h)
    assert all(h[n] == 2 ** n - 1 for n in range(11))

    # Reci sa parnim brojem nula: a(n) = a(n-1) + 3^(n-1), a(0) = 1
    a = niz_iteracijom(1, [0, 1], [1], 10, lambda n: 3 ** (n - 1))
    print("Parno nula:", a)
    assert all(a[n] == (3 ** n + 1) // 2 for n in range(11))

    # Prave u ravni: r(n) = r(n-1) + n, r(0) = 1
    r = niz_iteracijom(1, [0, 1], [1], 10, lambda n: n)
    print("Oblasti:", r)
    assert all(r[n] == 1 + n * (n + 1) // 2 for n in range(11))
    print("Sve provere prosle. OK")
