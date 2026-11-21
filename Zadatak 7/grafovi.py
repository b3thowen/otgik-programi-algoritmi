# Pomocne procedure za Zadatak 7 (uvodni pojmovi teorije grafova).
# Svi ostali programi uvoze ovaj fajl, pa svi fajlovi treba da budu u istom folderu.
from itertools import combinations, permutations


def prost_graf(V, E):
    """Pravi prost neusmeren graf (V, E). Grane se pamte kao dvoelementni skupovi."""
    V = list(V)
    if len(V) == 0:
        raise ValueError("skup cvorova mora biti neprazan")
    if len(set(V)) != len(V):
        raise ValueError("cvorovi moraju biti razliciti")
    grane = set()
    for (u, v) in E:
        if u == v:
            raise ValueError("prost graf nema petlje")
        if u not in V or v not in V:
            raise ValueError("kraj grane nije cvor grafa")
        grane.add(frozenset((u, v)))
    return (V, grane)


def stepeni(G):
    V, E = G
    d = {v: 0 for v in V}
    for e in E:
        for v in e:
            d[v] += 1
    return d


def susedi(G):
    V, E = G
    s = {v: set() for v in V}
    for e in E:
        u, v = tuple(e)
        s[u].add(v)
        s[v].add(u)
    return s


def niz_stepena(G):
    return sorted(stepeni(G).values(), reverse=True)


def oznake(G):
    """Za svaki cvor: (stepen, uredjen niz stepena suseda). To je invarijanta izomorfizma."""
    d = stepeni(G)
    s = susedi(G)
    return {v: (d[v], tuple(sorted(d[w] for w in s[v]))) for v in G[0]}


def je_izomorfizam(G1, G2, h):
    """Proverava da li je h (recnik) izomorfizam G1 u G2, direktno po definiciji."""
    V1, E1 = G1
    V2, E2 = G2
    if set(h.keys()) != set(V1) or set(h.values()) != set(V2) or len(set(h.values())) != len(V1):
        return False
    for u, v in combinations(V1, 2):
        if (frozenset((u, v)) in E1) != (frozenset((h[u], h[v])) in E2):
            return False
    return True


def potrebni_uslovi(G1, G2):
    """Vraca listu uslova koji ne vaze. Prazna lista znaci da su svi uslovi ispunjeni."""
    greske = []
    if len(G1[0]) != len(G2[0]):
        greske.append("razlicit broj cvorova")
    if len(G1[1]) != len(G2[1]):
        greske.append("razlicit broj grana")
    if niz_stepena(G1) != niz_stepena(G2):
        greske.append("razlicit graficki niz")
    if sorted(oznake(G1).values()) != sorted(oznake(G2).values()):
        greske.append("razlicite oznake cvorova (stepen i stepeni suseda)")
    return greske


def nadji_izomorfizam(G1, G2):
    """Backtracking pretraga. Vraca jedan izomorfizam (recnik) ili None."""
    if potrebni_uslovi(G1, G2):
        return None
    V1, E1 = G1
    V2, E2 = G2
    o1, o2 = oznake(G1), oznake(G2)
    poredak = sorted(V1, key=lambda v: -o1[v][0])   # cvorovi opadajuce po stepenu
    h = {}
    iskoriscen = set()
    n = len(V1)

    def prosiri(k):
        if k == n:
            return True
        u = poredak[k]
        for w in V2:
            if w in iskoriscen or o2[w] != o1[u]:
                continue
            ok = True
            for i in range(k):
                x = poredak[i]
                if (frozenset((x, u)) in E1) != (frozenset((h[x], w)) in E2):
                    ok = False
                    break
            if ok:
                h[u] = w
                iskoriscen.add(w)
                if prosiri(k + 1):
                    return True
                del h[u]
                iskoriscen.discard(w)
        return False

    return dict(h) if prosiri(0) else None


def svi_izomorfizmi_grubom_silom(G1, G2):
    """Proverava svih n! bijekcija. Koristi se samo za male grafove, radi provere."""
    V1, E1 = G1
    V2, E2 = G2
    if len(V1) != len(V2):
        return []
    rez = []
    for p in permutations(V2):
        h = dict(zip(V1, p))
        if je_izomorfizam(G1, G2, h):
            rez.append(h)
    return rez


def podgraf(G, V1, E1):
    """Proverava da li je (V1, E1) podgraf grafa G: V1 podskup V, E1 podskup E, E1 u C(V1, 2)."""
    V, E = G
    if not set(V1) <= set(V):
        return False
    E1 = {frozenset(e) for e in E1}
    if not E1 <= E:
        return False
    return all(e <= set(V1) for e in E1)


def razapinjuci_podgraf(G, V1, E1):
    return podgraf(G, V1, E1) and set(V1) == set(G[0])


def indukovani_podgraf(G, V1):
    """Podgraf indukovan skupom cvorova V1: sve grane iz E ciji su oba kraja u V1."""
    V, E = G
    V1 = [v for v in V if v in set(V1)]
    return (V1, {e for e in E if e <= set(V1)})


def oduzmi_granu(G, e):
    V, E = G
    return (list(V), E - {frozenset(e)})


def oduzmi_cvor(G, v):
    V, E = G
    return ([x for x in V if x != v], {e for e in E if v not in e})


def kompletan(n):
    V = list(range(1, n + 1))
    return prost_graf(V, combinations(V, 2))


def kompletan_bipartitan(m, n):
    A = ["a%d" % i for i in range(1, m + 1)]
    B = ["b%d" % i for i in range(1, n + 1)]
    return prost_graf(A + B, [(x, y) for x in A for y in B])


def kontura(n):
    V = list(range(1, n + 1))
    return prost_graf(V, [(i, i % n + 1) for i in range(1, n + 1)])


def hiperkocka(n):
    V = list(range(2 ** n))
    return prost_graf(V, [(u, u ^ (1 << i)) for u in V for i in range(n) if u < u ^ (1 << i)])


def disjunktna_unija(G1, G2):
    V1, E1 = G1
    V2, E2 = G2
    ren = {v: ("y", v) for v in V2}
    V = [("x", v) for v in V1] + [ren[v] for v in V2]
    E = [(("x", min(tuple(e), key=str)), ("x", max(tuple(e), key=str))) for e in E1]
    E += [(ren[min(tuple(e), key=str)], ren[max(tuple(e), key=str)]) for e in E2]
    return prost_graf(V, E)
