class Kocka:
    """
    Trieda reprezentuje hraciu kocku.
    """

    def __init__(self, pocet_stien = 6):
        self.__pocet_stien = pocet_stien

    def vrat_pocet_stien(self):
        """
        Vrati pocet stien kocky.
        :return:
        """
        return self.__pocet_stien

    def hod(self):
        """
        Vykona hod kockou a vrati cislo od 1 po pocet stien.
        """
        import random as _random
        return _random.randint(1, self.__pocet_stien)

    def __str__(self):
        """
        Vracia textovu reprezentaciu kocky.
        """
        return str("Kocka s {0} stenami".format(self.__pocet_stien))

# vytvorenie kociek
kocka6 = Kocka()
kocka10 = Kocka(10)

# hod kockou 6
print(kocka6)
for _ in range(10):
    print(kocka6.hod(), end = " ")

# hod kockou 10
print("\n", kocka10)
for _ in range(10):
    print(kocka10.hod(), end = " ")
