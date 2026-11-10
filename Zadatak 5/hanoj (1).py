# Zadatak 5 - hanojske kule: h(n) = 2h(n-1) + 1

brojac = 0

def hanoj(n, od, ka, pomocni, ispis=True):
    """Premesta n diskova sa stapa od na stap ka, koristeci pomocni."""
    global brojac
    if n == 0:
        return
    hanoj(n - 1, od, pomocni, ka, ispis)
    brojac += 1
    if ispis:
        print(f"disk {n} sa {od} na {ka}")
    hanoj(n - 1, pomocni, ka, od, ispis)


if __name__ == "__main__":
    print("n = 3:")
    hanoj(3, "A", "C", "B")
    print("Broj koraka:", brojac)
    assert brojac == 2 ** 3 - 1
    for n in range(1, 11):
        brojac = 0
        hanoj(n, "A", "C", "B", ispis=False)
        assert brojac == 2 ** n - 1
    print("Za n od 1 do 10 broj koraka je 2 na n minus 1. OK")
