def validateImageSize(imageUrls, maxSize):
    # byteSizes: {
    #     'kn': 1000,
    #     'mn': 1000000,
    #     'nn': 1000000000 
    # }
    sizeOfArr = len(imageUrls)
    returnArr = []
    if maxSize == 'none':
        maxSizeInt = 1000000
    else:
        digit = int("".join(i for i in maxSize if i.isdigit()))
        cha = "".join(i for i in maxSize if i.isalpha()).lower()
        if cha == 'kb':
            maxSizeInt = digit*1000
        elif cha == 'mb':
            maxSizeInt = digit*1000000
        else:
            maxSizeInt = digit*1000000000
    for i in range(sizeOfArr):
        sizeOfImage = int(imageUrls[i][1])
        if sizeOfImage > maxSizeInt:
            returnArr.append([imageUrls[i][0], 'FALSE'])
        else:
            returnArr.append([imageUrls[i][0], 'TRUE'])
    return returnArr

j= [['https://svs.gsfc.nasa.gov/vis/a030000/a030800/a030877/frames/5760x3240_16x9_01p/BlackMarble_2016_928m_conus_labeled.png', '32000000']]
k = '20MB'
print(validateImageSize(j,'none'))