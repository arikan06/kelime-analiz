#wikipedi sayfası var mı yok mu  hangi ekler geliyor onu da yapcam gerçek bir kelime olup olmadığına bakcak sonra gerçek kelimeyse ingilizcesini yazcak gerçek kelimeyse sözlük anlamını yazcak etimolojisini falan yazcak
# harfleri rastgele karıştırıp rastgele bir cümle oluşturmak
#şapkalı harfler
#google translate girip atıyorum kullanıcı merto yazdı merto'nun bütün dilleri taratarak gerçek bir kelime mi kelimeyse hangi dilde olduğunu ve ne anlama geldiğini türkçe yazacak
#benzer kelimeler
#mesela kullanıcı 12 harfli a ile başlayan diyor program o kelimeleri bulsun
unlu = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
kalinUnlu = ['a', 'ı', 'o', 'u']
inceUnlu = ['e', 'i', 'ö', 'ü', ]

unsuz = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
sertUnsuz = ['p', 'ç', 't', 'k', 's', 'ş', 'h', 'f']
yumusakUnsuz = ['b', 'c', 'd', 'g', 'ğ', 'j', 'l', 'm', 'n', 'r','v', 'y', 'z']

turkce = ['ı', 'ğ', 'ü', 'ş', 'İ', 'ö', 'ç']

def mertfsmal():
    time.sleep(0.06)
    print("""                       _    __                     _""")
    time.sleep(0.06)
    print("""                      | |  / _|                   | |""")
    time.sleep(0.06)
    print("""   _ __ ___   ___ _ __| |_| |_ ___ _ __ ___   __ _| |""")
    time.sleep(0.06)
    print("""  | '_ ` _ \ / _ \ '__| __|  _/ __| '_ ` _ \ / _` | |""")
    time.sleep(0.06)
    print("""  | | | | | |  __/ |  | |_| | \__ \ | | | | | (_| | |""")
    time.sleep(0.06)
    print("""  |_| |_| |_|\___|_|   \__|_| |___/_| |_| |_|\__,_|_|""")
    time.sleep(0.06)
    print()
    time.sleep(0.5)
    print('Github: github.com/mertfsmal')
    time.sleep(0.5)
    print('Repository: https://github.com/mertfsmal/kelime-analiz')
    time.sleep(0.5)
    print('Discord: mrt#0269')
    time.sleep(0.5)
    print('Kaynaklar: www.kelimeler.net, www.etimolojiturkce.com, www.sozluk.gov.tr')

def kucuk(kucuklestir):
    kucuklestir = kucuklestir.replace("İ", "i")
    kucuklestir = kucuklestir.replace("I", "ı")
    kucuklestir = kucuklestir.lower()
    return kucuklestir

def ingilizce(ingilizcelestir):
    ingilizcelestir = ingilizcelestir.replace("İ", "i")
    ingilizcelestir = ingilizcelestir.lower()
    ingilizcelestir = ingilizcelestir.replace("ı", "i")
    ingilizcelestir = ingilizcelestir.replace("ş", "s")
    ingilizcelestir = ingilizcelestir.replace("ç", "c")
    ingilizcelestir = ingilizcelestir.replace("ğ", "g")
    ingilizcelestir = ingilizcelestir.replace("ö", "o")
    ingilizcelestir = ingilizcelestir.replace("ü", "u")
    return ingilizcelestir

def etimolojiTurkce(aranacak):
    res = requests.get(f'https://www.etimolojiturkce.com/kelime/{aranacak}')
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    if soup.title.string == '404 Not Found':
        print(f'"{aranacak}" kelimesinin etimolojisi bulunamadı.')
    else:
        print(f'"{aranacak}" kelimesinin etimolojisi bulundu.')

def harfListe(yazdir, kelime, liste,):
    say=0
    for harf in kelime:
        if harf in liste:
            say = say + 1
    print(yazdir, say)

def kelimelernet(aranacak):
    if len(aranacak)-1 >= 1:
        aranacak=ingilizce(aranacak.replace('.', ''))
        if len(aranacak.split()) >= 2:
            #input(f'harfimiz: {aranacak.split()[0]}, komudumuz: {aranacak.split()[1]}')
            print()
            if aranacak.split()[1] == 'baslayan' or 'biten':
                if aranacak.split()[1] == 'baslayan':
                    res = requests.get(f'https://kelimeler.net/{aranacak.split()[0]}-ile-baslayan-kelimeler')
                    soup = bs4.BeautifulSoup(res.text, "html.parser")
                    aciklama = soup.find('p').get_text().split()
                    print(aciklama[0], aciklama[1], aciklama[2], aciklama[3], aciklama[4], aciklama[5],)
                if aranacak.split()[1] == 'biten':
                    res = requests.get(f'https://kelimeler.net/{aranacak.split()[0]}-ile-biten-kelimeler')
                    soup = bs4.BeautifulSoup(res.text, "html.parser")
                    print(soup.title.string)
            else:
                print('Yanlış kullanım. Komudunuz "baslayan" veya "biten" olmalı')
        else:
            print('Yanlış kullanım. Yazdığınız komut 2 kelime veya 2 kelimeden fazla olmalı.')
    else:
        print(' "." ile başlayıp devamını getirmedin.')

def sozlukgovtr(aranacak):
    if len(aranacak.split()) != 1:
        print(f'sadece 1 kelime arayabilirsiniz. ({len(aranacak.split())} tane kelime aramayı denediniz.)')
    else:
        res = requests.get(f'https://sozluk.gov.tr/gts?ara={aranacak}')
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        bilgi = json.loads(res.text)
        #print(bilgi)
        if str(soup) == '{"error":"Sonuç bulunamadı"}':
            print(f'{aranacak} kelimesi sozluk.gov.tr adresinde bulunamadı.')
        else:
            for i in range(int(bilgi[0]['anlam_say'])):
                time.sleep(0.8)
                print(f'{i+1}. anlamı:', bilgi[0]['anlamlarListe'][i]['anlam'])
            print('Cümle içerisinde örnek:', bilgi[0]['anlamlarListe'][0]['orneklerListe'][0]['ornek'])
            print('Birleşikler:', bilgi[0]['birlesikler'])

def uygulama():
    while True:
        time.sleep(0.6)
        print()
        analiz=kucuk(input('Analiz edilecek kelimeyi girin. '))
        if analiz.startswith('.'):
            kelimelernet(analiz)
        else:
            print('-')
            print('Genel bilgi:')
            print("Kelime sayısı:",len(analiz.split()))
            print('Toplam harf:', len(analiz)-len(analiz.split())+1)
            for kelime in analiz.split():
                time.sleep(0.6)
                print('-')
                print(f'{kelime} kelimesinin analizi:')
                harfListe('ünlü ve hece sayısı:', kelime, unlu)
                harfListe('Kalın ünlü harflerin sayısı:', kelime, kalinUnlu)
                harfListe('İnce ünlü harflerin sayısı:', kelime, inceUnlu)
                harfListe('Ünsüz harflerin sayısı:', kelime, unsuz)
                harfListe('Yumuşak ünsüz harflerin sayısı:', kelime, yumusakUnsuz)
                harfListe('Sert ünsüz harflerin sayısı:', kelime, sertUnsuz)
                harfListe('Türkçe harflerin sayısı:', kelime, turkce)
                etimolojiTurkce(kelime)
                sozlukgovtr(kelime)

if __name__ == '__main__':
    try:
        import json
        import time
        import requests
        import bs4
        mertfsmal()
        uygulama()
    except ModuleNotFoundError:
        import pip
        pip.main(['install requests'])
        pip.main(['install bs4'])
    #except HTTPSConnectionPool:
    #    print('Siteye bağlanılamadı.')
    #    input()
    except Exception as e:
        print(e)
        input()
        pass
