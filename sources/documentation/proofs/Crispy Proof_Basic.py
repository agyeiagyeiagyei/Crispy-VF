from pyNewsApi import PYNEWS
import io, os, glob

variableFontPath = '/Users/aamacbook/Work Interim/Crispy-VF/font/variable_ttf/Crispy[SRIF,wdth,wght]-VF.ttf'

# print(os.getcwd())

texts = []

for filename in os.listdir("texts"):
    textFilePath = os.getcwd()+"/texts/"+filename
    with open(textFilePath, "r", encoding="utf-8") as f:
        textString = f.read()
    texts.append(textString)
    
for proofStrings in texts:
    
allCapSpacingString = "HAHBHCHDHEHFHGHHHIHJHKHLHMHNHOHHHPHQHRHSHTHUHVHWHXHYHZH \n OAOBOCODOEOFOGOHOIOJOKOLOMONOOOOOPOQOROSOTOUOVOWOXOYOZO"

spacingStringBox = (40, 0, 690, 500)

def randomHeadline():
    news = PYNEWS()
    data = news.get_headline_by_source(source='google-news')
    return data[randint(0, len(data))]["title"]

def calcTextSizeForBox(txt, box, minSize=5, maxSize=300, tolerance=0.1):
    #this should get refactored for a binary search
    fs = (minSize + maxSize) / 2
    
    fontSize(fs)
    lineHeight(fs)
    overflow = textOverflow(txt, box)
    if overflow:
        while overflow:
            fs += -0.5
            fontSize(fs)
            lineHeight(fs)
            overflow = textOverflow(txt, box)
    else:
        while not overflow:
            fs += 0.5
            fontSize(fs)
            lineHeight(fs)
            overflow = textOverflow(txt, box)
    return fs


def pageLabel(instanceName):
    font("")
    text(str(instanceName), (40, height() - 40))

def makeProof():
    for instanceName, setupMatrix in listNamedInstances(variableFontPath).items():
        newPage("LetterLandscape")
        print(instanceName, setupMatrix)
        pageLabel(instanceName)
        font(variableFontPath)
        fontVariations(wght= setupMatrix['wght'], wdth = setupMatrix['wdth'], SRIF = setupMatrix['SRIF'])
        fs = calcTextSizeForBox(allCapSpacingString, spacingStringBox)
        print(fs)
        fontSize(fs*0.7)
        lineHeight(fs*0.8)
        spacingText = textBox(allCapSpacingString, spacingStringBox, align="left")
        newPage("LetterLandscape")
        pageLabel(instanceName)
        font(variableFontPath)
        fontVariations(wght= setupMatrix['wght'], wdth = setupMatrix['wdth'], SRIF = setupMatrix['SRIF'])
        fs = calcTextSizeForBox(randomHeadline().upper(), spacingStringBox)
        print(fs)
        fontSize(fs*0.7)
        lineHeight(fs*0.8)
        spacingText = textBox(randomHeadline().upper(), spacingStringBox, align="left")
        
# print(data)
        
# makeProof()
# saveImage("Crispy Proof.pdf")