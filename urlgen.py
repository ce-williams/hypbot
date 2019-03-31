# BaseURL =  "http://www.adidas.com/us/BB9043.html?forceSelSize=BB9043_600"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def URLgen(model, size):
    BaseSize = 500
    # BaseSize is for Shoe Size 6.5
    ShoeSize = int(Size) - 6.5
    ShoeSize = int(ShoeSize) * 20
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'http://www.adidas.com/us/' + str(Model) + '.html?forceSelSize=' + str(Model) + '_' + str(ShoeSizeCode)
    return URL

Model = input('Model #: ')
Size = input('Size: ')

URL = URLgen(Model, Size)

print(URL)
