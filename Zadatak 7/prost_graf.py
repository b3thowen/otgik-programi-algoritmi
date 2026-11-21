# Prost graf, lema o zbiru stepena i specijalne klase grafova.
from math import comb
from grafovi import prost_graf, stepeni, niz_stepena, kompletan, kompletan_bipartitan, kontura, hiperkocka

print("Prost graf G: V = {a, b, c, d, e}, E = {ab, ac, bc, cd, de}")
G = prost_graf("abcde", [("a", "b"), ("a", "c"), ("b", "c"), ("c", "d"), ("d", "e")])
d = stepeni(G)
print("  stepeni:", d)
print("  graficki niz:", niz_stepena(G))
print("  zbir stepena =", sum(d.values()), ", 2|E| =", 2 * len(G[1]))
neparni = [v for v in G[0] if d[v] % 2 == 1]
print("  cvorovi neparnog stepena:", neparni, "(paran broj)")
assert sum(d.values()) == 2 * len(G[1]) and len(neparni) % 2 == 0

print("Pokusaj pravljenja grafa sa petljom i sa nepostojecim cvorom:")
for E in ([("a", "a")], [("a", "z")]):
    try:
        prost_graf("abc", E)
    except ValueError as greska:
        print("  odbijeno:", greska)

print("Specijalne klase (cvorovi, grane, graficki niz):")
for n in range(2, 8):
    K = kompletan(n)
    assert len(K[1]) == comb(n, 2) and set(stepeni(K).values()) == {n - 1}
for (m, n) in [(2, 2), (3, 2), (3, 3), (4, 5)]:
    K = kompletan_bipartitan(m, n)
    assert len(K[0]) == m + n and len(K[1]) == m * n
    print("  K(%d,%d): %d cvorova, %d grana, niz %s" % (m, n, len(K[0]), len(K[1]), niz_stepena(K)))
for n in range(3, 8):
    C = kontura(n)
    assert len(C[1]) == n and set(stepeni(C).values()) == {2}
for n in range(1, 6):
    Q = hiperkocka(n)
    assert len(Q[0]) == 2 ** n and len(Q[1]) == n * 2 ** (n - 1) and set(stepeni(Q).values()) == {n}
    print("  Q%d: %d cvorova, %d grana, svi stepeni jednaki %d" % (n, len(Q[0]), len(Q[1]), n))
print("  K(n) ima C(n,2) grana, a svi stepeni su n-1, provereno za n = 2..7")
print("Sve provere prosle. OK")
