import  requests
import os
import  threading
import  bs4

os.mkdir('xkcd',exist_ok=True)

def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))

        res =requests.get('http://xkcd.com/%s' %(urlNumber))

        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image.

        comicElem = soup.select('#comic img')

        if comicElem == []:
            print('could not find comic img')

        else:
            comicUrl= comicElem[0].get('src')

            # down load the image

            res = requests.get(comicUrl)
            res.raise_for_status()

            # save image to ./xkcd

            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)


            imageFile.close()

# 创建并启动线程

downloadThreads = []

for i in range(0,1400,100):
    downloadThread = threading.Thread(target=downloadXkcd,args=(i,i+99))

    downloadThreads.append(downloadThread)

    downloadThread.start()

# 等待所有线程结束

for downloadThread in downloadThreads:
    downloadThread.join()

print('done')








