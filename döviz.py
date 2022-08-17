from random import betavariate
import socket, time, requests
from bs4 import BeautifulSoup #html ve xml dosyalarını işlememizi sağlayan kütüphane
import tkinter as tk 

#internet bağlantısını kontrol ettiğimiz kısım
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.google.com", 80))
    s.close()
    print("Bağlanılıyor")
except Exception:
    print("Lütfen İnternet Bağlantınızı Kontrol Ediniz")
    time.sleep(3) #3 saniye sonra programı kapatır
    exit()

url = "https://www.doviz.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

#verileri çektiğimiz kısım burası

data = soup.find("span", {"data-socket-key":"gram-altin"}).text
data1 = soup.find("span", {"data-socket-key":"USD"}).text
data2 = soup.find("span", {"data-socket-key":"EUR"}).text
data3 = soup.find("span", {"data-socket-key":"GBP"}).text
data4 = soup.find("span", {"data-socket-key":"XU100"}).text
data5 = soup.find("span", {"data-socket-key":"bitcoin"}).text

#uygulama olarak açılmasını sağlayan kısım burası

window = tk.Tk()
window.geometry("310x270")
window.title("Borsa")
window.configure(background="spring green")

#yazıları oluşturduğumuz kısım

label = tk.Label(window, text="Borsa", font="arial 15 bold", bg="spring green")
label.pack()

gramaltin = tk.Label(window, text="Gram Altın", font="arial 12", bg="spring green")
gramaltin.pack()
gramaltin.place(x=30,y=45)
goldvalue= tk.Label(window, text=data, font="arial 12", bg="spring green" )
goldvalue.pack()
goldvalue.place(x=30,y=65)

dolar = tk.Label(window, text="Dolar", font="arial 12", bg="spring green")
dolar.pack()
dolar.place(x=200,y=45)
dolarvalue= tk.Label(window, text=data1, font="arial 12", bg="spring green" )
dolarvalue.pack()
dolarvalue.place(x=200,y=65)

euro = tk.Label(window, text="Euro", font="arial 12", bg="spring green")
euro.pack()
euro.place(x=30,y=115)
eurovalue= tk.Label(window, text=data2, font="arial 12", bg="spring green" )
eurovalue.pack()
eurovalue.place(x=30,y=135)

sterlin = tk.Label(window, text="Sterlin", font="arial 12", bg="spring green")
sterlin.pack()
sterlin.place(x=200,y=115)
sterlinvalue= tk.Label(window, text=data3, font="arial 12", bg="spring green" )
sterlinvalue.pack()
sterlinvalue.place(x=200,y=135)

bist = tk.Label(window, text="Bist", font="arial 12", bg="spring green")
bist.pack()
bist.place(x=30,y=185)
bistvalue= tk.Label(window, text=data4, font="arial 12", bg="spring green" )
bistvalue.pack()
bistvalue.place(x=30,y=205)

bitcoin = tk.Label(window, text="Bitcoin", font="arial 12", bg="spring green")
bitcoin.pack()
bitcoin.place(x=200,y=185)
bitcoinvalue= tk.Label(window, text=data5, font="arial 12", bg="spring green" )
bitcoinvalue.pack()
bitcoinvalue.place(x=200,y=205)

window.mainloop()


