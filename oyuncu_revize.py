import time
import random
import sys

class BaseClass():
    def __init__(self):
        self.oyuncu_tecrube = 0
        self.oyuncu_can = 0  #guncelle_cn() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_mana = 0 #guncelle_mg() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_stamina = 0 #guncelle_pw() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_max_can = 0 #max_can() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_max_mana = 0 #max_mana() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_max_stamina = 0 #max_stamina() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_darbeemmeoranı = 0 #guncelle_cn() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_buyucuthac0 = 0 #guncelle_mg() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_buyucudefans = 0 #guncelle_mg() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_savascıthac0 = 0 #guncelle_pw() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_savascıdefans = 0 #guncelle_pw() göre hesaplanır buyucu,savascı,npc initinde
        self.oyuncu_pw = 0  #buyucu veya savascı sınıfına göre değişir...
        self.oyuncu_mg = 0 #buyucu veya savascı sınıfına göre değişir...
        self.oyuncu_cn = 0 #buyucu veya savascı sınıfına göre değişir...
        self.oyuncu_yetenek_puanı = 0
        self.oyuncu_yetenek_havuz = self.oyuncu_pw + self.oyuncu_mg + self.oyuncu_cn
        self.oyuncu_heal_pot = 2
        self.oyuncu_mana_pot = 2
        self.oyuncu_stamina_pot = 2
        self.oyuncu_buyu_damage = 0  #buyucu veya savascı, npc sınıfına göre değişir...
        self.oyuncu_kılıc_damage = 0 ##buyucu veya savascı, npc sınıfına göre değişir...
        self.oyuncu_kritik_vurma_olasılık = random.randint(0, 5)
        self.oyuncu_max_vurma_oran = (random.randint(50, 100) / 100)  # buyu_damage %kaçı kadar vuracaksın?
        self.oyuncu_hedef_buyucudefans = 20
        self.oyuncu_hedef_savascıdefans = 20
        self.oyuncu_hedef_can = 0
        self.oyuncu_hedef_isim = ""
        self.saldırı_turu = ""
        self.zar = 1
        
    def guncelle_cn(self):
        if 0 <= self.oyuncu_cn < 5:
            self.oyuncu_darbeemmeoranı = 0.01
            self.oyuncu_can = 60

        elif 5 <= self.oyuncu_cn < 10:
            self.oyuncu_darbeemmeoranı = 0.05
            self.oyuncu_can = 80

        elif 10 <= self.oyuncu_cn < 15:
            self.oyuncu_darbeemmeoranı = 0.10
            self.oyuncu_can = 100

        elif 15 <= self.oyuncu_cn < 20:
            self.oyuncu_darbeemmeoranı = 0.15
            self.oyuncu_can = 120

        elif self.oyuncu_cn == 20:
            self.oyuncu_darbeemmeoranı = 0.20
            self.oyuncu_can = 160
            
    def guncelle_mg(self):
        if 0 <= self.oyuncu_mg < 5:
            self.oyuncu_buyucuthac0 = 20
            self.oyuncu_buyucudefans = 12
            self.oyuncu_mana = 60

        elif 5 <= self.oyuncu_mg < 10:
            self.oyuncu_buyucuthac0 = 19
            self.oyuncu_buyucudefans = 10
            self.oyuncu_mana = 80

        elif 10 <= self.oyuncu_mg < 15:
            self.oyuncu_buyucuthac0 = 18
            self.oyuncu_buyucudefans = 8
            self.oyuncu_mana = 100

        elif 15 <= self.oyuncu_mg < 20:
            self.oyuncu_buyucuthac0 = 15
            self.oyuncu_buyucudefans = 6
            self.oyuncu_mana = 120

        elif self.oyuncu_mg == 20:
            self.oyuncu_buyucuthac0 = 10
            self.oyuncu_buyucudefans = 2
            self.oyuncu_mana = 160

    def guncelle_pw(self):
        if 0 <= self.oyuncu_pw < 5:
            self.oyuncu_savascıthac0 = 20
            self.oyuncu_savascıdefans = 12
            self.oyuncu_stamina = 60

        elif 5 <= self.oyuncu_pw < 10:
            self.oyuncu_savascıthac0 = 19
            self.oyuncu_savascıdefans = 10
            self.oyuncu_stamina = 80

        elif 10 <= self.oyuncu_pw < 15:
            self.oyuncu_savascıthac0 = 18
            self.oyuncu_savascıdefans = 8
            self.oyuncu_stamina = 100

        elif 15 <= self.oyuncu_pw < 20:
            self.oyuncu_savascıthac0 = 15
            self.oyuncu_savascıdefans = 6
            self.oyuncu_stamina = 120

        elif self.oyuncu_pw == 20:
            self.oyuncu_savascıthac0 = 10
            self.oyuncu_savascıdefans = 2
            self.oyuncu_stamina = 160

    def max_can(self):
        if 0 <= self.oyuncu_cn < 5:
            self.oyuncu_max_can = 60

        elif 5 <= self.oyuncu_cn < 10:
            self.oyuncu_max_can = 80

        elif 10 <= self.oyuncu_cn < 15:
            self.oyuncu_max_can = 100

        elif 15 <= self.oyuncu_cn < 20:
            self.oyuncu_max_can = 120

        elif self.oyuncu_cn == 20:
            self.oyuncu_max_can = 160
        

    def max_mana(self):
        if 0 <= self.oyuncu_mg < 5:
            self.oyuncu_max_mana = 60

        elif 5 <= self.oyuncu_mg < 10:
            self.oyuncu_max_mana = 80

        elif 10 <= self.oyuncu_mg < 15:
            self.oyuncu_max_mana = 100

        elif 15 <= self.oyuncu_mg < 20:
            self.oyuncu_max_mana = 120

        elif self.oyuncu_mg == 20:
            self.oyuncu_max_mana = 160

    def max_stamina(self):
        if 0 <= self.oyuncu_pw < 5:
            self.oyuncu_max_stamina = 60

        elif 5 <= self.oyuncu_pw < 10:
            self.oyuncu_max_stamina = 80

        elif 10 <= self.oyuncu_pw < 15:
            self.oyuncu_max_stamina = 100

        elif 15 <= self.oyuncu_pw < 20:
            self.oyuncu_max_stamina = 120

        elif self.oyuncu_pw == 20:
            self.oyuncu_max_stamina = 160

    def seviye(self):
        return 1 if self.oyuncu_tecrube in range(0,101) else (2 if self.oyuncu_tecrube in range(101,201) else
                                                             (3 if self.oyuncu_tecrube in range(201,501) else
                                                             (4 if self.oyuncu_tecrube in range(501,901) else
                                                                 print("şimdilik max seviye"))))
    def seviye_yukselt(self):
        pass

    def buyu_upgrade(self):
        self.oyuncu_buyu_damage += self.oyuncu_buyu_damage*0.15
        print("Tebrikler büyü gücün arttı!!!".center(50, "#"))
    #buyu saldırı türünde kullanılan buyu_damage i oyundaki özel kutu,olaylara göre upgrade eder.

    def kılıc_upgrade(self):
        self.oyuncu_kılıc_damage  += self.oyuncu_kılıc_damage*0.15
        print("Tebrikler kılıç gücün arttı!!!".center(50, "#"))

    def can_sınırı(self):
        if 0 <= self.oyuncu_cn < 5 and self.oyuncu_can > 60:
            self.oyuncu_can=60
        elif 5 <= self.oyuncu_cn < 10 and self.oyuncu_can > 80:
            self.oyuncu_can = 80
        elif 10 <= self.oyuncu_cn < 15 and self.oyuncu_can > 100:
            self.oyuncu_can = 100
        elif 15 <= self.oyuncu_cn < 20 and self.oyuncu_can > 120:
            self.oyuncu_can = 120
        elif self.oyuncu_cn == 20 and self.oyuncu_can > 160:
            self.oyuncu_can = 160
        #aşağıda yetenek puanlarının alabileceği maksimum can miktarına göre; eğer pot kullanıp
        #maksimum can miktarını aşarsak yetenek puanına(cn) göre maksimum cana çekiyor.
        #maksimum cana çekmesi için iki şart yenilenmeden sonra canın maksimum candan yüksek olucak(can>60)
        #daha düşük olmucak(40 gibi),yetenek puanına göre(0<=self.oyuncu_cn<5) maksimum cana (self.oyuncu_can=60) çekilcek.

    def mana_sınırı(self):
        if 0 <= self.oyuncu_mg < 5 and self.oyuncu_mana > 60:
            self.oyuncu_mana = 60
        elif 5 <= self.oyuncu_mg < 10 and self.oyuncu_mana > 80:
            self.oyuncu_mana = 80
        elif 10 <= self.oyuncu_mg < 15 and self.oyuncu_mana > 100:
            self.oyuncu_mana = 100
        elif 15 <= self.oyuncu_mg < 20 and self.oyuncu_mana > 120:
            self.oyuncu_mana = 120
        elif self.oyuncu_mg==20 and self.oyuncu_mana > 160:
            self.oyuncu_mana = 160
        
    def stamina_sınırı(self):
        if 0 <= self.oyuncu_pw < 5 and self.oyuncu_stamina > 60:
            self.oyuncu_stamina = 60
        elif 5 <= self.oyuncu_pw < 10 and self.oyuncu_stamina > 80:
            self.oyuncu_stamina = 80
        elif 10 <= self.oyuncu_pw < 15 and self.oyuncu_stamina > 100:
            self.oyuncu_stamina = 100
        elif 15 <= self.oyuncu_pw < 20 and self.oyuncu_stamina > 120:
            self.oyuncu_stamina = 120
        elif self.oyuncu_pw == 20 and self.oyuncu_stamina > 160:
            self.oyuncu_stamina = 160

    @classmethod        
    def zaman(cls):
        for i in range(20):
            time.sleep(.1)
            print("\\.//", sep="", end="", flush=True)
        
    def heal_potic(self):
        if self.oyuncu_heal_pot < 1:
            print("Olamaz iyileştirme iksiri kalmamış!!!".center(65, "#"))
            self.secim()
        print("Yenilenme iksiri içiliyor".center(65, "."))
        self.zaman()
        print("\n")
        print(self.oyuncu_can,"yenilenmeden önce")
        print("\n",self.oyuncu_max_can*0.40, "kadar canın yenilendi".center(35, "!"))
        self.oyuncu_heal_pot -= 1
        self.oyuncu_can = self.oyuncu_can + self.oyuncu_max_can*0.40
        #aşağıda yetenek puanlarının alabileceği maksimum can miktarına göre; eğer pot kullanıp
        #maksimum can miktarını aşarsak yetenek puanına(cn) göre maksimum cana çekiyor.
        #maksimum cana çekmesi için iki şart yenilenmeden sonra canın maksimum candan yüksek olucak(can>60)
        #daha düşük olmucak(40 gibi),yetenek puanına göre(0<=self.oyuncu_cn<5) maksimum cana (self.oyuncu_can=60) çekilcek.
        self.can_sınırı()
        print(self.oyuncu_can, "yenilenmeden sonra")
        self.secim()

    def mana_potic(self):
        if self.oyuncu_mana_pot<1:
            print("Olamaz mana iksiri kalmamış!!!".center(65, "#"))
            self.secim()
        print("Mana iksiri içiliyor".center(65, "."))
        self.zaman()
        print("\n")
        print(self.oyuncu_mana, "yenilenmeden önce")
        print("\n", self.oyuncu_max_mana*0.40, "kadar manan yenilendi".center(35, "!"))
        self.oyuncu_mana_pot -= 1
        self.oyuncu_mana = self.oyuncu_mana + self.oyuncu_max_mana*0.40
        self.mana_sınırı()
        print(self.oyuncu_mana, "yenilenmeden sonra")
        self.secim()

    def stamina_potic(self):
        if self.oyuncu_stamina_pot < 1:
            print("Olamaz stamina iksiri kalmamış!!!".center(65, "#"))
            self.secim()
        print("Stamina iksiri içiliyor".center(65, "."))
        self.zaman()
        print("\n")
        print(self.oyuncu_stamina, "yenilenmeden önce")
        print("\n", self.oyuncu_max_stamina*0.40, "kadar staminan yenilendi".center(35, "!"))
        self.oyuncu_stamina_pot -= 1
        self.oyuncu_stamina = self.oyuncu_stamina + self.oyuncu_max_stamina*0.40
        self.stamina_sınırı()
        print(self.oyuncu_stamina, "yenilenmeden sonra")
        self.secim()

    def can_kuyu(self):
        print("yenilenme öncesi", self.oyuncu_can)
        print("Parlak ışıklar saçan kuyuya ilerliyorsun".center(100, "#"))
        print("Işık seni etrafını kapladı,bir saniye kendinden geçtin".center(100, "#"))
        self.zaman()
        self.guncelle_cn()
        print("\n", "Yenilendin")
        print("Yenileme sonrası", self.oyuncu_can)

    def mana_kuyu(self):
        print("yenilenme öncesi", self.oyuncu_mana)
        print("Gökkuşağının indiği o parlak kuyuya ilerliyorsun".center(100, "#"))
        print("Masmavi bir ışık etrafında girdap gibi dönüyor.".center(100, "#"))
        self.zaman()
        self.guncelle_mg()
        print("\n", "Yenilendin")
        print("Yenileme sonrası", self.oyuncu_mana)

    def stamina_kuyu(self):
        print("yenilenme öncesi", self.oyuncu_stamina)
        print("İhtişamlı bir savaşçı heykeline ilerliyorsun".center(100, "#"))
        print("Yorgunluğun azalmaya kendini daha dinç hissetmeye başladın.".center(100, "#"))
        self.zaman()
        self.guncelle_pw()
        print("\n", "Yenilendin")
        print("Yenileme sonrası", self.oyuncu_stamina)


    def secim(self):
        metin=input("""Saldırmak için s , Kaçmak için k, iyileşme için h, mana için m, stamina için st,oyun çıkış q:\t""".ljust(125))
        if metin == "s":
            self.saldır()
        elif metin == "k":
            self.kac()
        elif metin == "h":
            self.heal_potic()
        elif metin == "m":
            self.mana_potic()
        elif metin == "st":
            self.stamina_potic()
        elif metin == "q":
            return
        else:
            print("Sadece s,k,h,m,st,q giriniz!!!".ljust(65))
            self.secim()

    def kac(self):
        x=random.randint(0,8)
        print("kaçış için 8'lık zar sonucu", x)
        print("Kaçılıyor".center(25, "!"))
        if 2 <x <= 8:
            self.zaman()
            print("\n","Kaçamadın,rakibin seni yakaladı".center(25, "!"))
            self.oyuncu_hedef_isim.saldır()
            #self.saldır()
        elif 0 <= x <= 2:
            self.zaman()
            print("\n","Zar zor kaçtın...".center(35, "!"))
            print("Bu noktada yeni olaya ya da selfsecime heal vss pot için")
            return  #sınıftan çıkış programın ilerleyen kodlarına devam için,quit programı tamamen kapatıyor.
            #bu aşamada heal vss pot için self.seçime veya yeni olaya...
        
    def yenileme(self):
        self.oyuncu_mana += 0.05*self.oyuncu_mana #her turda yenilenme
        self.oyuncu_stamina += 0.05*self.oyuncu_stamina #her turda yenilenme
        self.oyuncu_can += 0.05*self.oyuncu_can #her turda yenilenme
        self.mana_sınırı()
        self.stamina_sınırı()
        self.can_sınırı()
        print(0.05*self.oyuncu_can, "can ", 0.05*self.oyuncu_mana, "mana ", 0.05*self.oyuncu_stamina, "stamina ", "yenilendi")

    def buyu_sozleri(self):
        self.buyu_sayac = random.randint(0,4)
        if self.buyu_sayac == 0:
            print("Ast kiranann kair, gardurm soth-arn".center(50))
        elif self.buyu_sayac == 1:
            print("Degang kuashnya, lampar terbong kilat mati yangjahat".center(50))
        elif self.buyu_sayac == 2:
            print("Jistrah tagopar ast moirparan kini!".center(50))
        elif self.buyu_sayac == 3:
            print("Burus longang degang birsih sekalilagang".center(50))
        elif self.buyu_sayac == 4:
            print("Ast bilak moiparalan suh akular tatangusar".center(50))
        
    def buyu_s(self):
        #buyu özel atak için
        if self.oyuncu_mana < 31:
            print("Mana yetersiz!!!".center(25, "!")) #mana yeterli mi kontrolu.
            self.secim() #mana yetersiz ise başka türlü saldırı ve diğer seçenekler için şans verme.
        self.oyuncu_mana-=30 #vurabilse de vuramasa da mana harcanır.
        if self.oyuncu_kritik_vurma_olasılık == 3:
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Kritik vuruş!!!")
            self.buyu_sozleri()
            self.zaman()
            return 2*3*(self.oyuncu_max_vurma_oran*self.oyuncu_buyu_damage) #2 kritik damage için,3 özel atak için
        else:
            #kritik vuramadığı zaman
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Normal vurdun")
            self.buyu_sozleri()
            self.zaman()
            return 3*(self.oyuncu_max_vurma_oran*self.oyuncu_buyu_damage)
        
    def buyu_n(self):
        if self.oyuncu_mana < 10:
            print("Mana yetersiz!!!".center(25, "!")) #mana yeterli mi kontrolu.
            self.secim() #mana yetersiz ise başka türlü saldırı ve diğer seçenekler için şans verme.
        self.oyuncu_mana-=10 #vurabilse de vuramasa da mana harcanır.
        if self.oyuncu_kritik_vurma_olasılık == 3:
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Kritik vuruş!!!")
            self.buyu_sozleri()
            self.zaman()
            return 2*(self.oyuncu_max_vurma_oran*self.oyuncu_buyu_damage) #2 kritik damage için
        else:
            #kritik vuramadığı zaman
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Normal vurdun")
            self.buyu_sozleri()
            self.zaman()
            return self.oyuncu_max_vurma_oran*self.oyuncu_buyu_damage

    def kılıc_s(self):
        if self.oyuncu_stamina < 31:
            print("Stamina yetersiz!!!".center(25, "!")) #stamina yeterli mi kontrolu.
            self.secim() #stamina yetersiz ise başka türlü saldırı ve diğer seçenekler için şans verme.
        self.oyuncu_stamina -= 30 #vurabilse de vuramasa da mana harcanır.
        if self.oyuncu_kritik_vurma_olasılık == 3:
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Kritik vuruş!!!")
            print("Kılıcın rakibin kafasını yardı".center(35, "!"))
            self.zaman()
            return 2*3*(self.oyuncu_max_vurma_oran*self.oyuncu_kılıc_damage) #2 kritik damage için,3 özel atak için
        else:
            #kritik vuramadığı zaman
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Normal vurdun")
            print("Kılıcın rakibin elini kopardı".center(65, "!"))
            self.zaman()
            return 3*(self.oyuncu_max_vurma_oran*self.oyuncu_kılıc_damage)

    def kılıc_n(self):
        if self.oyuncu_stamina < 10:
            print("Stamina yetersiz!!!".center(25,"!")) #stamina yeterli mi kontrolu.
            self.secim() #stamina yetersiz ise başka türlü saldırı ve diğer seçenekler için şans verme.
        self.oyuncu_stamina-=10 #vurabilse de vuramasa da mana harcanır.
        if self.oyuncu_kritik_vurma_olasılık == 3:
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Kritik vuruş!!!")
            print("Zorlada olsa kılıcın rakibi kötü yaraladı".center(35,"!"))
            self.zaman()
            return 2*(self.oyuncu_max_vurma_oran*self.oyuncu_kılıc_damage) #2 kritik damage için
        else:
            #kritik vuramadığı zaman
            #print("oyuncu kritik vurma olasılık(3 ise kritik):\t",self.oyuncu_kritik_vurma_olasılık) #kontrol
            #print("oyuncu max vurma oranı",self.oyuncu_max_vurma_oran) #kontrol
            print("Normal vurdun")
            print("Rakip kılıc saldırında az bir yara ile kurtardı".center(65,"!"))
            self.zaman()
            return self.oyuncu_max_vurma_oran*self.oyuncu_kılıc_damage
        

    def yirmilikzar(self):
        self.zar = random.randint(1, 20)
        return self.zar

    def vurdumu(self):
        # handikapları ilk satırlara
        if self.saldırı_turu == "bs":
            self.oyuncu_buyucuthac0 += 3  # vurup vurmama olasılığı öncesi handikap.zar atılmadan önce geçici handikap
            print("Oyuncu handikaplı buyucuthac0:\t",self.oyuncu_buyucuthac0)
            if self.yirmilikzar() >= self.oyuncu_buyucuthac0 - self.oyuncu_hedef_buyucudefans:
                print("npc buyucudefans:\t",self.oyuncu_hedef_buyucudefans) #kontrol
                print("Oyuncunun attığı yirmilik zar:\t",self.zar)  
                return True
            self.oyuncu_buyucuthac0 -= 3 #Vuruş başarısız handikap geri al.
            print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
            print("Özel büyü saldırı başarısız oyuncu handikapsız buyucuthac0: ",self.oyuncu_buyucuthac0) #konrol
            return False
        
        if self.saldırı_turu == "ks":
            self.oyuncu_savascıthac0 += 3  # vurup vurmama olasılığı öncesi handikap.zar atılmadan önce geçici handikap
            print("Oyuncu handikaplı savascıthac0:\t",self.oyuncu_savascıthac0)
            if self.yirmilikzar() >= self.oyuncu_savascıthac0 - self.oyuncu_hedef_savascıdefans:
                print("npc savascıdefans:\t",self.oyuncu_hedef_savascıdefans) #kontrol
                print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
                return True
            self.oyuncu_savascıthac0 -= 3 #Vuruş başarısız handikap geri al.
            print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
            print("Özel kılıç saldırı başarısız oyuncu handikapsız savascıthac0: ",self.oyuncu_savascıthac0) #kontrol
            return False

        if self.saldırı_turu == "bn":
            if self.yirmilikzar() >= self.oyuncu_buyucuthac0 - self.oyuncu_hedef_buyucudefans:
                print("npc buyucudefans:\t",self.oyuncu_hedef_buyucudefans) #kontrol
                print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
                return True
            print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
            return False

        if self.saldırı_turu == "kn":
            if self.yirmilikzar() >= self.oyuncu_savascıthac0 - self.oyuncu_hedef_savascıdefans:
                print("npc savascıdefans:\t",self.oyuncu_hedef_savascıdefans) #kontrol
                print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
                return True
            print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
            return False 
        #saldırı turu buyu ise self.oyuncu_hedef_buyucudefans,saldırı turu kılıc ise self.oyuncu_hedef_savascıdefans

    def saldır_kontrol(self):
        self.condition = [self.saldırı_turu == "", self.saldırı_turu != "bs", self.saldırı_turu != "bn",
                          self.saldırı_turu != "ks", self.saldırı_turu != "kn"]
        if any(self.condition):
            return True
    # condition değişkenine atanan liste compare condition(karşılaştırma koşulu) içerir.
    # any() fonksiyonu aldığı parametreye atanan argument'ın içerdeği öğelerden biri bile bool değeri (bool() hatırla) True olsa True değeri döndürür.
    # all() fonksiyonu aldığı parametreye atanan argument'ın içerdeği öğelerden hepsinin bool değeri (bool() hatırla) True olsa True değeri döndürür.

    def saldır(self):
        self.saldırı_turu=input("Özel büyü saldırı için bs, normal büyü saldırı için bn, Özel kılıç saldırı için ks, normal kılıç saldırı için kn".ljust(150))
        print("hedef sınıf örnek:\t", self.oyuncu_hedef_isim)
        if not self.vurdumu():
            #print("Oyuncunun attığı yirmilik zar:\t",self.zar)  # kontrol
            print("Rakibin etkilenmedi...".center(35,"!"))
            #self.yenileme() bunu açarsan vuramasan bile yenileme yapıyor çok güçlü oluyorsun.buraya belli şarta bağlı olarak self.yenileme()
            #çalıştıran fonksiyon ekle
            print("#############OYUNCU TURN BİTİŞ#################")
            self.oyuncu_hedef_isim.saldır()   #imp1 yerine oyuncu_revize.py de değişkene ata self.oyuncu_hedef_isim="" default
            #imp1.saldır() oyun.py de imp1=imp() rakip saldırır
            #if karşılaştırma ifadesi True ise elif koşuluna geçilmez.False ise elif koşuluna geçilir.
            #Aşağı satırlar vuruş başarılı olduğu için işler.if not self.vurdumu() karşılaştırma operatoru sonucu False ise...
            
        elif self.saldırı_turu == "bs":
            self.oyuncu_buyucuthac0 -= 3
            print("Handikapsız buyucuthac0:\t",self.oyuncu_buyucuthac0)
            #self.vurdumu() fonksiyonunda zar atılmadan önce geçici olarak konulan handikapı kaldırır.
            print("Saldırı öncesi oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı öncesi npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.oyuncu_hedef_isim.oyuncu_can=self.oyuncu_hedef_isim.oyuncu_can-self.buyu_s() #imp1 yerine oyuncu.py de değişkene ata self.oyuncu_hedef_isim="" default
            print("\n")
            print("Saldırı sonrası oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı sonrası npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.yenileme()
            #print(self.oyuncu_hedef_isim,"'e",self.buyu_s(),"kadar zarar verdin")
            #Yukarıdaki # etkisiz hale getirilen satırda self.buyu_s tekrar çalıştırılır,ekstra mana harcanır.buyu_s random olarak her çalıştırılışta farklı bir
            #değer döndürdüğünden sağlıklı sonuç vermiyor.
            #eğer self.oyuncu_hedef_isim.can<1 rakip öldü exp kazan ve yeni olay Olay1'e aktar.
            if self.oyuncu_hedef_isim.oyuncu_can < 0:
                print("Rakibin öldü burada self.oyuncu_tecrube ye ekleme yap ve olay1'e aktar")
                return
            print("#############OYUNCU TURN BİTİŞ#################")
            self.oyuncu_hedef_isim.saldır()
            
        elif self.saldırı_turu == "bn":
            print("Saldırı öncesi oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı öncesi npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.oyuncu_hedef_isim.oyuncu_can=self.oyuncu_hedef_isim.oyuncu_can-self.buyu_n() #imp1 yerine oyuncu.py de değişkene ata self.oyuncu_hedef_isim="" default
            print("\n")
            print("Saldırı sonrası oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı sonrası npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.yenileme()
            #print(self.oyuncu_hedef_isim,"'e",self.buyu_n(),"kadar zarar verdin")
            #Yukarıdaki # etkisiz hale getirilen satırda self.buyu_n tekrar çalıştırılır,ekstra mana harcanır.buyu_n random olarak her çalıştırılışta farklı bir
            #değer döndürdüğünden sağlıklı sonuç vermiyor.
            #eğer self.oyuncu_hedef_isim.can<1 rakip öldü exp kazan ve yeni olay Olay1'e aktar.
            if self.oyuncu_hedef_isim.oyuncu_can < 0:
                print("Rakibin öldü burada self.oyuncu_tecrube ye ekleme yap ve olay1'e aktar")
                return
            print("#############OYUNCU TURN BİTİŞ#################")
            self.oyuncu_hedef_isim.saldır()

        elif self.saldırı_turu == "ks":
            self.oyuncu_savascıthac0 -= 3
            print("Handikapsız savascıthac0:\t",self.oyuncu_savascıthac0)
            #self.vurdumu() fonksiyonunda zar atılmadan önce geçici olarak konulan handikapı kaldırır.
            print("Saldırı öncesi oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı öncesi npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.oyuncu_hedef_isim.oyuncu_can=self.oyuncu_hedef_isim.oyuncu_can-self.kılıc_s() #imp1 yerine oyuncu.py de değişkene ata self.oyuncu_hedef_isim="" default
            print("\n")
            print("Saldırı sonrası oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı sonrası npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.yenileme()
            #print(self.oyuncu_hedef_isim,"'e",self.kılıc_s(),"kadar zarar verdin")
            #Yukarıdaki # etkisiz hale getirilen satırda self.kılıc_s tekrar çalıştırılır,ekstra stamina harcanır.kılıc_s random olarak her çalıştırılışta farklı bir
            #değer döndürdüğünden sağlıklı sonuç vermiyor.
            #eğer self.oyuncu_hedef_isim.can<1 rakip öldü exp kazan ve yeni olay Olay1'e aktar.
            if self.oyuncu_hedef_isim.oyuncu_can < 0:
                print("Rakibin öldü burada self.oyuncu_tecrube ye ekleme yap ve olay1'e aktar")
                return
            print("#############OYUNCU TURN BİTİŞ#################")
            self.oyuncu_hedef_isim.saldır()

        elif self.saldırı_turu == "kn":
            print("Saldırı öncesi oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı öncesi npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.oyuncu_hedef_isim.oyuncu_can=self.oyuncu_hedef_isim.oyuncu_can-self.kılıc_n() #imp1 yerine oyuncu.py de değişkene ata self.oyuncu_hedef_isim="" default
            print("\n")
            print("Saldırı sonrası oyuncu","can: ",self.oyuncu_can,"mana: ",self.oyuncu_mana,"stamina: ",self.oyuncu_stamina)
            print("Saldırı sonrası npc can:",self.oyuncu_hedef_isim.oyuncu_can,"mana: ",self.oyuncu_hedef_isim.oyuncu_mana,"stamina: ",self.oyuncu_hedef_isim.oyuncu_stamina) #kontrol
            self.yenileme()
            #print(self.oyuncu_hedef_isim,"'e",self.kılıc_n(),"kadar zarar verdin")
            #Yukarıdaki # etkisiz hale getirilen satırda self.kılıc_n tekrar çalıştırılır,ekstra mana harcanır.kılıc_n random olarak her çalıştırılışta farklı bir
            #değer döndürdüğünden sağlıklı sonuç vermiyor.
            #eğer self.oyuncu_hedef_isim.can<1 rakip öldü exp kazan ve yeni olay Olay1'e aktar.
            if self.oyuncu_hedef_isim.oyuncu_can < 0:
                print("Rakibin öldü burada self.oyuncu_tecrube ye ekleme yap ve olay1'e aktar")
                return
            print("#############OYUNCU TURN BİTİŞ#################")
            self.oyuncu_hedef_isim.saldır()
        self.secim()

class Buyucu(BaseClass):
    def __init__(self,isim,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.isim=isim
        self.oyuncu_cn=10
        self.oyuncu_pw=8
        self.oyuncu_mg=15
        self.oyuncu_buyu_damage=15
        self.oyuncu_kılıc_damage=10
        self.guncelle_cn()
        self.guncelle_mg()
        self.guncelle_pw()
        self.max_mana()
        self.max_can()
        self.max_stamina()
        #BaseClass() baseclass miras alınan nitelik,metodlardan self.oyuncu_cn=10,self.oyuncu_pw=8,self.oyuncu_mg=15
        #sınıfın(buyucu.savascı.imp vs...) özelliğine göre değiştirilip sonra;
        #self.guncelle_cn(),self.guncelle_mg(),self.guncelle_pw() fonksiyonları yardımıyla sınıfa özel instance attribute
        #değerleri belirlenir.

class Savascı(BaseClass):
    def __init__(self,isim,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.isim=isim
        self.oyuncu_cn=10
        self.oyuncu_pw=15
        self.oyuncu_mg=8
        self.oyuncu_buyu_damage=10
        self.oyuncu_kılıc_damage=15
        self.guncelle_cn()
        self.guncelle_mg()
        self.guncelle_pw()
        self.max_mana()
        self.max_can()
        self.max_stamina()

class Imp(BaseClass):
    def __init__(self,isim,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.isim=isim
        self.oyuncu_cn=4
        self.oyuncu_pw=9
        self.oyuncu_mg=16
        self.oyuncu_buyu_damage = 12
        self.oyuncu_kılıc_damage = 8
        self.alınan_zarar = 0
        self.imp_hedef_buyucudefans = 20
        self.imp_hedef_savascıdefans = 20
        self.imp_hedef_can=0
        self.imp_hedef_isim=""
        self.guncelle_cn()
        self.guncelle_mg()
        self.guncelle_pw()
        self.max_mana()
        self.max_can()
        self.max_stamina()

    def imp_vurdumu(self):
        if self.yirmilikzar() >= self.oyuncu_buyucuthac0 - self.imp_hedef_buyucudefans:
            print("Oyuncu buyucudefans:\t",self.imp_hedef_buyucudefans) #kontrol
            print("Npc atılan yirmilik zar:\t",self.zar)  # kontrol
            return True
        #eğer imp buyu damage verirse...
        #if self.yirmilikzar() >= self.oyuncu_savascıthac0 - self.imp_hedef_savascıdefans:
            #print(self.zar)  # kontrol
            #return True
        #eğer imp kılıc damage verirse...
        print("Npc atılan yirmilik zar:\t",self.zar)  # kontrol
        return False

    def mana_yenileme(self):
        self.oyuncu_mana = self.oyuncu_mana + self.oyuncu_max_mana*0.1
        self.mana_sınırı()
        print(self.oyuncu_max_mana*0.1,"mana ","yenilendi")
        #super().yenileme() #base classtaki yenileme() fonksiyonunu çalıştırır.super() fonksiyonu ile
        
    def saldır(self):
        print("hedef sınıf örnek:\t",self.imp_hedef_isim)
        if not self.imp_vurdumu():
            print("Rakibin sana vuruşu seni pes geçti")
            print("#############NPC TURN BİTİŞ#################")
            self.imp_hedef_isim.secim() #buyucu1 yerine self.imp_hedef_isim oyun.py de imp1.imp_hedef_isim=buyucu1
            #vuramadımı npc mana harcama...

        elif self.oyuncu_mana < 5:
            print("Mana yetersiz".center(50,"!"))
            self.mana_yenileme()
            self.imp_hedef_isim.secim()
        
        self.oyuncu_mana-=8     
        #npc saldırısının mana kullanması eksik.mana yetersiz ise self.imp_hedef_isim.secim()
        print("Npc saldırı öncesi oyuncu can: ",self.imp_hedef_isim.oyuncu_can) #kontrol
        print("Npc saldırı öncesi oyuncu mana: ",self.imp_hedef_isim.oyuncu_mana) #kontrol
        print("Npc saldırı öncesi oyuncu stamina: ",self.imp_hedef_isim.oyuncu_stamina) #kontrol
        self.imp_hedef_isim.oyuncu_can = self.imp_hedef_isim.oyuncu_can - (self.imp_buyu() - self.imp_buyu()*self.imp_hedef_isim.oyuncu_darbeemmeoranı)
        print("--------------------------------------------------------------")
        if self.imp_hedef_isim.oyuncu_can < 0:
            print("ÖLDÜN".center(50,"!"))
            quit()
        print("Npc saldırı sonrası oyuncu can: ",self.imp_hedef_isim.oyuncu_can) #kontrol
        print("Npc saldırı sonrası oyuncu mana: ",self.imp_hedef_isim.oyuncu_mana) #kontrol
        print("Npc saldırı sonrası oyuncu stamina: ",self.imp_hedef_isim.oyuncu_stamina) #kontrol
        print("Rakibin sana vurdu... yaralandın",self.imp_buyu(),"zarar gördün")
        print("#############NPC TURN BİTİŞ#################")
        self.imp_hedef_isim.secim() #buyucu1 yerine self.imp_hedef_isim oyun.py de imp1.imp_hedef_isim=buyucu1

    def imp_buyu(self):
        return self.oyuncu_buyu_damage*self.oyuncu_max_vurma_oran

#saldır() da bs,bn,ks,kn dışında bir şey girdiğimde saldırıyor ama hangi saldırı??? kontrol bs,bn,ks,kn dışında
#giriş olursa self.saldıra yönlendir.
#imp sınıfı saldırıda mana azalması sonucu mana biterse nasıl bir adil sistem koyarak savaştırabilirim?
#rakibe verilen zararı kesin şekilde hesaplamak.çünkü buyu_s,kılıc_s,buyu_n,kılıc_n her çalıştırılışta mana veya stamina harcıyor.
#ve her çalıştırılışta random değer döndürdüğünden ilk kullanıştaki damage değerini nasıl sabitleyebilirim?

    
    
        








