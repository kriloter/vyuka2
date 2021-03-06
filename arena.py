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

class Bojovnik:
    """
    Trieda reprezentuje bojovnika v arene.
    """

    def __init__(self, meno, zivot, utok, obrana, kocka):
        """
        meno - meno bojovnika
        zivot - maximalny zivot
        utok - utok bojovnika
        obrana - obrana bojovnika
        kocka - instancia kocky
        """
        self.__meno = meno
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kocka = kocka

    def __str__(self):
        """
        Vracia textovu reprezentaciu bojovnika.
        """
        return str(self.__meno)

    def __repr__(self):
        """
        Co ja viem ...
        """
        return str(self.__meno)

    @property
    def nazive(self):
        return self.__zivot > 0

    @property
    def utok(self):
        return self.__utok

    @property
    def obrana(self):
        return self.__obrana

    @property
    def zivot(self):
        return "{0}/{1}".format(self.__zivot, self.__max_zivot)

    def graficky_zivot(self):
        """
        Graficka reprezentacia zivota bojovnika.
        """
        celkom = 20
        pocet = int(self.__zivot / self.__max_zivot * celkom)
        if (pocet == 0 and self.nazive):
            pocet = 1
        return "[{0}{1}]".format("#"*pocet, " "*(celkom - pocet))

    def bran_sa(self, uder):
        """
        Obrana
        """
        zranenie = uder - (self.__obrana + self.__kocka.hod())
        if zranenie > 0:
            self.__zivot = self.__zivot - zranenie
            if self.__zivot < 0:
                self.__zivot = 0

    def utoc(self, super):
        uder = self.__utok + self.__kocka.hod()
        super.bran_sa()



kocka = Kocka(10)
bojovnik_1 = Bojovnik("Bananko", 100, 20, 10, kocka)
print("Bojovnik: {0}".format(bojovnik_1))
print("Zivot: {0}".format(bojovnik_1.zivot))
print("Utok: {0}".format(bojovnik_1.utok))
print("Obrana: {0}".format(bojovnik_1.obrana))
print("Nazive: {0}".format(bojovnik_1.nazive))
print("Zivot: {0}".format(bojovnik_1.graficky_zivot()))
