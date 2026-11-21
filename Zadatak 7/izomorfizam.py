# Izomorfizam prostih grafova: primeri, potrebni uslovi i algoritam sa vracanjem.
from grafovi import (prost_graf, potrebni_uslovi, nadji_izomorfizam, je_izomorfizam,
                     svi_izomorfizmi_grubom_silom, niz_stepena, kompletan_bipartitan,
                     kontura, disjunktna_unija)


def izvestaj(naziv, G1, G2):
    print(naziv)
    print("  broj cvorova:", len(G1[0]), len(G2[0]), " broj grana:", len(G1[1]), len(G2[1]))
    print("  graficki nizovi:", niz_stepena(G1), niz_stepena(G2))
    print("  neispunjeni potrebni uslovi:", potrebni_uslovi(G1, G2) or "nema")
    h = nadji_izomorfizam(G1, G2)
    svi = svi_izomorfizmi_grubom_silom(G1, G2)
    print("  izomorfizam:", h if h else "ne postoji")
    print("  broj svih izomorfizama (pregled svih n! bijekcija):", len(svi))
    assert (h is not None) == (len(svi) > 0)
    if h:
        assert je_izomorfizam(G1, G2, h)
    return h, svi


print("PRIMER 1: dva izomorfna grafa")
G1 = prost_graf("abcde", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "a"), ("a", "c")])
G2 = prost_graf([1, 2, 3, 4, 5], [(1, 3), (1, 4), (2, 4), (2, 5), (3, 5), (3, 4)])
h, svi = izvestaj("G1 (kontura abcde sa tetivom ac) i G2", G1, G2)
h0 = {"a": 3, "b": 1, "c": 4, "d": 2, "e": 5}
print("  trazeni izomorfizam iz teksta je ispravan:", je_izomorfizam(G1, G2, h0))
assert je_izomorfizam(G1, G2, h0) and len(svi) == 2
print("  pogresna funkcija a->1, b->2, c->3, d->4, e->5 je izomorfizam:",
      je_izomorfizam(G1, G2, {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}))

print("PRIMER 2: isti broj cvorova, grana i isti graficki niz, a nisu izomorfni")
C6 = kontura(6)
dva_trougla = disjunktna_unija(kontura(3), kontura(3))
izvestaj("C6 i dva disjunktna trougla", C6, dva_trougla)
K33 = kompletan_bipartitan(3, 3)
prizma = prost_graf([1, 2, 3, 4, 5, 6],
                    [(1, 2), (2, 3), (1, 3), (4, 5), (5, 6), (4, 6), (1, 4), (2, 5), (3, 6)])
izvestaj("K(3,3) i trostrana prizma (oba povezana)", K33, prizma)
trouglovi = sum(1 for x in K33[0] for y in K33[0] for z in K33[0]
                if len({x, y, z}) == 3 and frozenset((x, y)) in K33[1]
                and frozenset((y, z)) in K33[1] and frozenset((x, z)) in K33[1])
print("  broj trouglova (preko uredjenih trojki) u K(3,3):", trouglovi, ", prizma ima trougao 1-2-3")

print("PRIMER 3: potrebni uslovi koji se vide odmah")
P4 = prost_graf([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4)])
zvezda = prost_graf([1, 2, 3, 4], [(1, 2), (1, 3), (1, 4)])
print("  put sa 4 cvora i zvezda K(1,3):", potrebni_uslovi(P4, zvezda))

print("PRIMER 4: osam cvorova, deset grana, graficki niz 3,3,3,3,2,2,2,2")
A = prost_graf("abcdefgh", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"),
                            ("e", "f"), ("f", "g"), ("g", "h"), ("h", "e"),
                            ("a", "e"), ("c", "g")])
B = prost_graf("abcdefgh", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"),
                            ("f", "g"), ("g", "h"), ("h", "a"), ("b", "f"), ("d", "h")])
izvestaj("Graf A (dva cetvorougla spojena sa dve grane) i graf B (osmougao sa dve tetive)", A, B)

print("PROVERA algoritma: nasumicni parovi grafova sa 6 cvorova, poredjenje sa pregledom svih bijekcija")
import random
random.seed(7)
V = list(range(6))
parovi = [(i, j) for i in V for j in V if i < j]
slaganja, izo = 0, 0
for _ in range(300):
    G = prost_graf(V, [e for e in parovi if random.random() < 0.5])
    p = V[:]
    random.shuffle(p)
    if random.random() < 0.5:
        # izomorfna kopija: preimenovanje cvorova
        H = prost_graf(V, [(p[u], p[v]) for (u, v) in map(tuple, G[1])])
    else:
        H = prost_graf(V, [e for e in parovi if random.random() < 0.5])
    a = nadji_izomorfizam(G, H) is not None
    b = len(svi_izomorfizmi_grubom_silom(G, H)) > 0
    slaganja += (a == b)
    izo += a
print("  poklapanja:", slaganja, "od 300, od toga izomorfnih parova:", izo)
assert slaganja == 300

print("Dve izomorfne konture C(9), cvorovi druge su nasumicno preimenovani:")
n = 9
p = list(range(1, n + 1))
random.shuffle(p)
Ca = kontura(n)
Cb = prost_graf(p, [(p[i - 1], p[i % n]) for i in range(1, n + 1)])
print("  izomorfizam nadjen:", nadji_izomorfizam(Ca, Cb) is not None)
print("Sve provere prosle. OK")
