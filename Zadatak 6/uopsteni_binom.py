# Uopsteni binomni koeficijent i uopstena binomna formula.
from fractions import Fraction
from math import comb
from stepeni_redovi import binom_uopsteni, binomni_red, mnozi, lepo

if __name__ == "__main__":
    print("Uopsteni binomni koeficijenti C(alfa, k), k = 0..5:")
    for alfa in (5, -1, -2, -3, Fraction(1, 2), Fraction(-1, 2)):
        print("alfa =", str(alfa).rjust(4), ":", lepo([binom_uopsteni(alfa, k) for k in range(6)]))

    # (1 + x)^(-2) = 1 - 2x + 3x^2 - 4x^3 + ...
    red = binomni_red(-2, 8)
    ocekivano = [(-1) ** n * (n + 1) for n in range(9)]
    assert red == ocekivano
    print("(1 + x)^(-2):", lepo(red))

    # (1 + x)^(1/2) = 1 + x/2 - x^2/8 + x^3/16 - 5x^4/128 + ...
    koren = binomni_red(Fraction(1, 2), 6)
    print("(1 + x)^(1/2):", lepo(koren))
    kvadrat = mnozi(koren, koren, 6)
    assert kvadrat == [1, 1, 0, 0, 0, 0, 0]
    print("Kvadrat reda daje 1 + x:", lepo(kvadrat))

    # (1 - x)^(-n): koeficijent uz x^k je C(n + k - 1, k)
    for n in (1, 2, 3, 5):
        red = [binom_uopsteni(-n, k) * (-1) ** k for k in range(10)]
        assert red == [comb(n + k - 1, k) for k in range(10)]
    print("(1 - x)^(-n) ima koeficijente C(n + k - 1, k), provereno za n = 1, 2, 3, 5.")

    # (1 - 4x)^(-1/2): koeficijent uz x^k je C(2k, k)
    red = [binom_uopsteni(Fraction(-1, 2), k) * (-4) ** k for k in range(10)]
    assert red == [comb(2 * k, k) for k in range(10)]
    print("(1 - 4x)^(-1/2):", lepo(red))

    # za nenegativan ceo alfa se poklapa sa obicnim binomnim koeficijentom
    for n in range(8):
        for k in range(10):
            assert binom_uopsteni(n, k) == comb(n, k)
    print("Za ceo alfa >= 0 poklapa se sa obicnim binomnim koeficijentom.")
    print("Sve provere prosle. OK")
