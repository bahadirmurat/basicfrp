#while True:
    #x=input("Oyuncu adını girin:\t")
    #y=input("buyucu için buyucu,savascı için savascı girin")
    #if not y=="buyucu" or not y=="savascı":
        #print("Sadece buyucu veya savascı girin!!!")
        #continue
    #import y  y nesnesini değişken olarak değil y isimli modül olarak algılıyor.
    #import oyuncu
    #import npc_imp #imp nesnesi,sınıf örneği oluşturucu
    #oyuncu1=y.y(x) #nesne,sınıf örneği
    #imp1=npc_imp.imp("herhangibirisim") #nesne,sınıf örneği
    #oyuncu1.hedef_defans=imp1.buyucudefans #saldırılacak npcye göre değiştir.
    #oyuncu1.rakip_isim="imp1"  oyuncu1 sabit

import oyuncu_revize
import olay1

print("imple karşılaştın")
imp1=oyuncu_revize.Imp("evil_imp")
buyucu1=oyuncu_revize.Buyucu("baha")
imp1.imp_hedef_buyucudefans=buyucu1.oyuncu_buyucudefans
imp1.imp_hedef_savascıdefans=buyucu1.oyuncu_savascıdefans
imp1.imp_hedef_can=buyucu1.oyuncu_can
imp1.imp_hedef_isim=buyucu1  #nesne(sınıf örneği ismi girsek olurmu?Olur)

buyucu1.oyuncu_hedef_buyucudefans=imp1.oyuncu_buyucudefans
buyucu1.oyuncu_hedef_savascıdefans=imp1.oyuncu_savascıdefans
buyucu1.oyuncu_hedef_can=imp1.oyuncu_can
buyucu1.oyuncu_hedef_isim=imp1 #nesne(sınıf örneği ismi girsek olurmu?Olur)

#Imp(),Buyucu() sınıfları GameBase() baseclasstan nitelik ve metodları miras
#aldığından;
#imp1.imp_hedef_buyucudefans=buyucu1.oyuncu_buyucudefans
#buyucu1.oyuncu_hedef_buyucudefans=imp1.oyuncu_buyucudefans
#kullanımda Imp(),Buyucu() sınıfında  self.guncelle_cn(),self.guncelle_mg()
#self.guncelle_pw() fonksiyonları yardımıyla buyucu1,imp1 sınıf örneğine özel
#olarak oyuncu_buyucudefans instance attribute değeri değişir.

buyucu1.secim()





        

    
    




