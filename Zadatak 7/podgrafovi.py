# Podgraf, pokrivajuci (razapinjuci) podgraf i podgraf indukovan skupom cvorova.
from itertools import combinations
from grafovi import (prost_graf, podgraf, razapinjuci_podgraf, indukovani_podgraf,
                     oduzmi_granu, oduzmi_cvor, kompletan)


def ispisi(naziv, G):
    V, E = G
    print("  %s: V = {%s}, E = {%s}" % (naziv, ", ".join(map(str, V)),
          ", ".join(sorted("".join(sorted(map(str, e))) for e in E))))


print("Graf G: V = {a, b, c, d, e, f}")
G = prost_graf("abcdef", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"),
                          ("f", "a"), ("a", "d"), ("b", "e")])
ispisi("G", G)

print("Podgraf H1 = ({a,b,c,d}, {ab, bc, cd})")
print("  da li je podgraf:", podgraf(G, "abcd", [("a", "b"), ("b", "c"), ("c", "d")]))
H1_grane = {frozenset(e) for e in [("a", "b"), ("b", "c"), ("c", "d")]}
print("  da li je H1 indukovan skupom {a,b,c,d}:", indukovani_podgraf(G, "abcd")[1] == H1_grane)
ispisi("indukovani podgraf skupom {a,b,c,d}", indukovani_podgraf(G, "abcd"))
print("  H1 nije indukovan, jer G ima granu ad, a H1 je nema")

print("Ono sto nije podgraf:")
print("  ({a,b,c}, {ac}) je podgraf:", podgraf(G, "abc", [("a", "c")]), "(ac nije grana grafa G)")
print("  ({a,c,d}, {ab}) je podgraf:", podgraf(G, "acd", [("a", "b")]), "(kraj grane b nije u skupu cvorova)")

print("Pokrivajuci podgraf: isti skup cvorova, deo grana")
ispisi("razapinjuci podgraf (V, {ab, bc, cd, de, ef})", (list(G[0]), {frozenset(e) for e in [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f")]}))
print("  provera:", razapinjuci_podgraf(G, "abcdef", [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f")]))
print("  H1 je razapinjuci podgraf:", razapinjuci_podgraf(G, "abcd", [("a", "b"), ("b", "c"), ("c", "d")]))

print("Oduzimanje grane i cvora:")
ispisi("G - ad", oduzmi_granu(G, ("a", "d")))
ispisi("G - a", oduzmi_cvor(G, "a"))

print("Prebrojavanje na grafu G (6 cvorova, 8 grana):")
svih_razapinjucih = 0
E = sorted(G[1], key=lambda e: sorted(e))
for k in range(len(E) + 1):
    for deo in combinations(E, k):
        assert razapinjuci_podgraf(G, G[0], [tuple(e) for e in deo])
        svih_razapinjucih += 1
print("  razapinjucih podgrafova:", svih_razapinjucih, "= 2^8 =", 2 ** 8)
assert svih_razapinjucih == 2 ** 8
indukovanih = 0
for k in range(1, 7):
    for W in combinations(G[0], k):
        H = indukovani_podgraf(G, W)
        assert podgraf(G, H[0], H[1])
        indukovanih += 1
print("  indukovanih podgrafova (neprazan skup cvorova):", indukovanih, "= 2^6 - 1 =", 2 ** 6 - 1)
assert indukovanih == 63

print("K6 indukovan skupom {a, c, d, f}:")
K6 = prost_graf("abcdef", combinations("abcdef", 2))
H = indukovani_podgraf(K6, "acdf")
print("  broj cvorova:", len(H[0]), ", broj grana:", len(H[1]), "(to je K4)")
assert len(H[1]) == 6
print("Sve provere prosle. OK")
