# Izomorfizam kao relacija ekvivalencije: provera osobina i prebrojavanje klasa.
from itertools import combinations, product
from grafovi import prost_graf, nadji_izomorfizam, je_izomorfizam, svi_izomorfizmi_grubom_silom


def svi_oznaceni(n):
    V = list(range(1, n + 1))
    parovi = list(combinations(V, 2))
    for maska in product([0, 1], repeat=len(parovi)):
        yield prost_graf(V, [p for p, m in zip(parovi, maska) if m])


def klase(grafovi):
    """Deli grafove na klase izomorfnosti. Svaki graf se poredi samo sa predstavnicima klasa."""
    pred, brojevi = [], []
    for G in grafovi:
        for i, P in enumerate(pred):
            if nadji_izomorfizam(P, G) is not None:
                brojevi[i] += 1
                break
        else:
            pred.append(G)
            brojevi.append(1)
    return pred, brojevi


print("Provera refleksivnosti, simetricnosti i tranzitivnosti na svim oznacenim grafovima sa 4 cvora")
G4 = list(svi_oznaceni(4))
print("  broj oznacenih grafova sa 4 cvora:", len(G4), "= 2^6")
ident = {v: v for v in range(1, 5)}
assert all(je_izomorfizam(G, G, ident) for G in G4)
print("  refleksivnost: identicko preslikavanje je izomorfizam svakog grafa u samog sebe. OK")
sim = 0
for G in G4[:20]:
    for H in G4:
        h = nadji_izomorfizam(G, H)
        if h is not None:
            inv = {w: v for v, w in h.items()}
            assert je_izomorfizam(H, G, inv)
            sim += 1
print("  simetricnost: za %d izomorfnih parova inverz izomorfizma je izomorfizam. OK" % sim)
tr = 0
for G in G4[:12]:
    for H in G4:
        h = nadji_izomorfizam(G, H)
        if h is None:
            continue
        for K in G4[:30]:
            g = nadji_izomorfizam(H, K)
            if g is not None:
                gh = {v: g[h[v]] for v in G[0]}
                assert je_izomorfizam(G, K, gh)
                tr += 1
print("  tranzitivnost: za %d trojki slaganje dva izomorfizma je izomorfizam. OK" % tr)

print("Broj klasa izomorfnosti (neizomorfnih prostih grafova):")
ocekivano = {2: 2, 3: 4, 4: 11, 5: 34}
for n in range(2, 6):
    pred, brojevi = klase(svi_oznaceni(n))
    print("  n = %d: %d klasa (ocekivano %d), ukupno oznacenih grafova %d" % (n, len(pred), ocekivano[n], sum(brojevi)))
    assert len(pred) == ocekivano[n] and sum(brojevi) == 2 ** (n * (n - 1) // 2)
    if n == 4:
        print("    velicine klasa za n = 4:", sorted(brojevi))

print("Grafovi sa 5 cvorova i 3 grane:")
G53 = [G for G in svi_oznaceni(5) if len(G[1]) == 3]
pred, brojevi = klase(G53)
print("  oznacenih grafova:", len(G53), ", klasa izomorfnosti:", len(pred))
assert len(pred) == 4
print("Sve provere prosle. OK")
