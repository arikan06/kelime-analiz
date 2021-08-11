#wikipedi sayfası var mı yok mu  hangi ekler geliyor onu da yapcam gerçek bir kelime olup olmadığına bakcak sonra gerçek kelimeyse ingilizcesini yazcak gerçek kelimeyse sözlük anlamını yazcak etimolojisini falan yazcak
# harfleri rastgele karıştırıp rastgele bir cümle oluşturmak
#şapkalı harfler
#google translate girip atıyorum kullanıcı merto yazdı merto'nun bütün dilleri taratarak gerçek bir kelime mi kelimeyse hangi dilde olduğunu ve ne anlama geldiğini türkçe yazacak
unluHarfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
kalinUnlu = ['a', 'ı', 'o', 'u']
inceUnlu = ['e', 'i', 'ö', 'ü', ]

unsuzHarfler = ['']
sertUnsuz = ['']
yumusakUnsuz = ['']

turkceHarfler = ['ı', 'ğ', 'ü', 'ş', 'İ', 'ö', 'ç']

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

def harfListe(cumle, kelime, liste,):
    say=0
    for harf in kelime:
        if harf in liste:
            say = say + 1
    print(cumle, say)

def uygulama():
    while True:
        analiz=kucuk(input('Analiz edilecek kelimeyi girin. '))

        print('-----------------------------------------------------------------------')
        print("Kelime sayısı:",len(analiz.split()))
        print('Toplam harf:', len(analiz)-len(analiz.split())+1)
        harfListe('hece ve ünlü sayısı:', analiz, unluHarfler)
        harfListe('Türkçe harflerin sayısı:', analiz, turkceHarfler)
        say=0
        for kelimeler in analiz.split():
            etimoloji(analiz.split()[say])
            say = say + 1
        print('-----------------------------------------------------------------------')

if __name__ == '__main__':
    try:
        import requests
        import bs4
        uygulama()
    except Exception as e:
        m=input('Hatayı görüntülemek için "e" yazın. ')
        if m=='e':
            print(e)
            input()
