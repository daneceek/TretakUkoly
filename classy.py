


class Škola:
    
    #constructor
    def __init__(self, na_co_je_skola, proc_do_ni_chodime):
        self.pica = na_co_je_skola 
        self.mrdat = proc_do_ni_chodime
    #     self.ukony_do_opravy = 1000

    # def krok_vpred(self):
    #     print("Robot udělal krok vpřed")
    #     self.ukony_do_opravy -= 1
    #     print(f"Úkony do kontroly: {self.ukony_do_opravy}")

    # def krok_vzad(self):
    #     print("Robot udělal krok vzad")
    #     self.ukony_do_opravy -= 1
    #     print(f"Úkony do kontroly: {self.ukony_do_opravy}")


kreten = Škola("na piču", "děkuji za pozornost")
print("definice školy:")
print(kreten.pica)
print(kreten.mrdat)

#objekty podle classy
# robot_1 = Robot(24,0.6)


# robot_2 = Robot(48, 0.5)
# robot_1.krok_vpred()
# robot_1.krok_vzad()
# print(robot_1.ukony_do_opravy)
# print(robot_2.ukony_do_opravy)
# print(f"Výdrž baterie je: {robot_1.bat}")
# print(f"Délka rukou je: {robot_1.del_ruk}")

