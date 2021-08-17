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

def kucuk(kucuklestir):
    kucuklestir = kucuklestir.replace("İ", "i")
    kucuklestir = kucuklestir.replace("I", "ı")
    kucuklestir = kucuklestir.lower()
    return kucuklestir

def etimoloji(aranacak):
    res = requests.get(f'https://www.etimolojiturkce.com/kelime/{aranacak}')
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    if soup.title.string == '404 Not Found':
        print(f'"{aranacak}" kelimesinin etimolojisi bulunamadı.')
    else:
        print(f'"{aranacak}" kelimeinin etimolojisi bulundu.')

def harfListe(yazdir, kelime, liste,):
    say=0
    for harf in kelime:
        if harf in liste:
            say = say + 1
    print(yazdir, say)

def uygulama():
    while True:
        time.sleep(0.6)
        print()
        analiz=kucuk(input('Analiz edilecek kelimeyi girin. '))
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
            etimoloji(kelime)

if __name__ == '__main__':
    try:
        import time
        import requests
        import bs4
        mertfsmal()
        uygulama()
    except Exception as e:
        m=input('Hatayı görüntülemek için "e" yazın. ')
        if m=='e':
            print(e)
            input()
