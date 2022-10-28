import mechanize
from time import sleep

browser =  mechanize.Browser()

browser.open('LINK AQUI')

f=open("source.html","wb")
f.write(browser.response().read())

filetypes=[".jpg",".JPEG",".jpeg",".png",".PNG"] 
myfiles=[]
for l in browser.links():
    for t in filetypes:
        if t in str(l):
            myfiles.append(l)

print('Total de itens: ', str(len(myfiles)))

def downloadlink(l):
    f=open(l.text,"wb")
    browser.click_link(l)
    f.write(browser.response().read())
    print(l.text," foi baixado")
    #br.back()

for l in myfiles:
    sleep(1)
    downloadlink(l)