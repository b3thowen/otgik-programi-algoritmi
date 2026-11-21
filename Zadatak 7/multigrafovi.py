# Usmeren i neusmeren multigraf, primeri i problem sedam mostova Kenigsberga.
from collections import Counter


def stepen_neusmeren(V, psi):
    d = {v: 0 for v in V}
    for e, (u, v) in psi.items():
        d[u] += 1
        d[v] += 1
    return d


def paralelne_neusmerene(psi):
    grupe = {}
    for e, (u, v) in psi.items():
        grupe.setdefault(frozenset((u, v)), []).append(e)
    return [sorted(g) for g in grupe.values() if len(g) > 1]


def paralelne_usmerene(psi):
    grupe = {}
    for e, uv in psi.items():
        grupe.setdefault(uv, []).append(e)
    return [sorted(g) for g in grupe.values() if len(g) > 1]


def ulazni_izlazni(V, psi):
    ul = {v: 0 for v in V}
    iz = {v: 0 for v in V}
    for e, (u, v) in psi.items():
        iz[u] += 1
        ul[v] += 1
    return ul, iz


def proveri_def(V, E, psi):
    assert len(V) > 0
    assert not (set(V) & set(E))
    assert set(psi.keys()) == set(E)
    for e, (u, v) in psi.items():
        assert u in V and v in V and u != v


print("Neusmeren multigraf: V = {a, b, c}")
V = ["a", "b", "c"]
E = ["e1", "e2", "e3", "e4"]
psi = {"e1": ("a", "b"), "e2": ("a", "b"), "e3": ("b", "c"), "e4": ("a", "c")}
proveri_def(V, E, psi)
d = stepen_neusmeren(V, psi)
print("  stepeni:", d, " zbir =", sum(d.values()), " 2|E| =", 2 * len(E))
print("  paralelne grane:", paralelne_neusmerene(psi))
assert sum(d.values()) == 2 * len(E)

print("Usmeren multigraf: V = {a, b, c, d}")
V = ["a", "b", "c", "d"]
E = ["e1", "e2", "e3", "e4", "e5", "e6"]
psi = {"e1": ("a", "b"), "e2": ("a", "b"), "e3": ("b", "a"),
       "e4": ("b", "c"), "e5": ("c", "d"), "e6": ("d", "a")}
proveri_def(V, E, psi)
ul, iz = ulazni_izlazni(V, psi)
print("  ulazni stepeni:", ul)
print("  izlazni stepeni:", iz)
print("  paralelne grane:", paralelne_usmerene(psi))
print("  e3 nije paralelna sa e1, jer je psi(e3) = (b, a) razlicito od (a, b)")
assert sum(ul.values()) == sum(iz.values()) == len(E)

print("Problem sedam mostova Kenigsberga")
V = ["A", "B", "C", "D"]   # A ostrvo Kenhof, B severna obala, C juzna obala, D istocni deo
psi = {"m1": ("A", "B"), "m2": ("A", "B"), "m3": ("A", "C"), "m4": ("A", "C"),
       "m5": ("A", "D"), "m6": ("B", "D"), "m7": ("C", "D")}
E = list(psi)
proveri_def(V, E, psi)
d = stepen_neusmeren(V, psi)
neparni = [v for v in V if d[v] % 2 == 1]
print("  stepeni:", d)
print("  zbir stepena =", sum(d.values()), ", broj mostova =", len(E))
print("  cvorova neparnog stepena:", len(neparni))
print("  Ojlerova tura (zatvorena) postoji samo ako su svi stepeni parni:", len(neparni) == 0)
print("  Ojlerov put postoji samo ako ima 0 ili 2 cvora neparnog stepena:", len(neparni) in (0, 2))
assert len(neparni) == 4 and sum(d.values()) == 14
print("Sve provere prosle. OK")
