def ortalama(veriler):
    return sum(veriler) / len(veriler)


def sigma(veriler):
    return round(
        (sum((x - ortalama(veriler)) ** 2 for x in veriler) / len(veriler)) ** 0.5, 3
    )


def s(veriler):
    return round(
        (sum((x - ortalama(veriler)) ** 2 for x in veriler) / (len(veriler) - 1))
        ** 0.5,
        3,
    )


def sigmakare(veriler):
    return round(sigma(veriler) ** 2, 3)


def skare(veriler):
    return round(s(veriler) ** 2, 3)


def mod(veriler):
    tekrar = {}
    for sayi in veriler:
        if sayi in tekrar:
            tekrar[sayi] += 1
        else:
            tekrar[sayi] = 1

    max_tekrar = max(tekrar.values())
    mod = [key for key, value in tekrar.items() if value == max_tekrar]

    return mod


def medyan(veriler):
    verileri_sirala = sorted(veriler)

    n = len(verileri_sirala)
    ortadeger = n // 2
    if n % 2 == 0:
        return (verileri_sirala[ortadeger - 1] + verileri_sirala[ortadeger]) / 2
    else:
        return verileri_sirala[ortadeger]


def standart_hata(veriler):
    return round(s(veriler) / (len(veriler) ** 0.5), 3)


def çeyreklikler(veriler):

    verileri_sirala = sorted(veriler)
    n = len(verileri_sirala)
    Q2 = medyan(verileri_sirala)
    if n % 2 == 0:
        Q1 = medyan(verileri_sirala[: n // 2])
        Q3 = medyan(verileri_sirala[n // 2 :])

    else:
        Q1 = medyan(verileri_sirala[: n // 2])
        Q3 = medyan(verileri_sirala[(n // 2) + 1 :])

    return Q1, Q2, Q3


def çeyreksapma(veriler):
    Q1, _, Q3 = çeyreklikler(veriler)
    return (Q3 - Q1) / 2
