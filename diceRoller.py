import random
import discord
import ast
import os 
from dotenv import load_dotenv

load_dotenv()

list = {    "d4": 4,
            "d6": 6,
            "d8": 8,
            "d10":10,
            "d12":12,
            "d20":20,
            "d100":100
        }

listAuthor = ast.literal_eval(os.getenv('LISTAUTHOR'))

calcDictionary= { 
                "Valeris":12,
                "Globiglob":16,
                "Dango":13,
                "Larynx":13,
                "Nevardo":14,
                "Kairox":16,
                "Bugs Bunny":10,
                "Kryssik":15,
            }

healthDictionary= { 
                "Valeris":45,
                "Globiglob":38,
                "Dango":38,
                "Larynx":38,
                "Nevardo":38,
                "Kairox":45,
                "Bugs Bunny":43,
                "Kryssik":59,
            }

healthDictionaryReset= {
                "Valeris":45,
                "Globiglob":52,
                "Dango":32,
                "Larynx":38,
                "Nevardo":56,
                "Kairox":51,
                "Bugs Bunny":43,
                "Kryssik":59,
            }

initiativeDictionary= {
                "Valeris":1,
                "Globiglob":3,
                "Dango":2,
                "Larynx":3,
                "Nevardo":2,
                "Kairox":3,
                "Bugs Bunny":0,
                "Kryssik":1,
            }
                
def __init__(self, diceNumber, diceFace):
        self.diceNumber = diceNumber
        self.diceFace = diceFace

def DiceRoll(diceNumber, diceFaceValue, diceFaceKey, messageAuthor):
    result = 0
    nick = AuthorChangeName(messageAuthor)
    print(f"Tirada de un {diceFaceKey} por {nick}")
    for x in range(diceNumber):
        resultRandom = random.randrange(1,diceFaceValue + 1)
        result += resultRandom
        print(f"tirada {x + 1} : {resultRandom}")
    if diceNumber == 1:
        if result == 20:

            return f"Tirada de un {diceFaceKey}, NAT 20 tu turno de brillar {nick}"
        
        return f"Tirada de un {diceFaceKey} por {nick}, resultado: {result}"
    else:
        return f"Tirada de un {diceFaceKey} por {nick}, resultado total: {result}"



def AuthorChangeName(messageAuthor):
    for x in listAuthor:
        if str(messageAuthor) == x:
            return listAuthor[x]
        else:
            return messageAuthor
    

def StringAnalizer(message_content, messageAuthor):
    resultString= ""
    resultList  = []
    diceNumberList = []
    diceFaceValueList = []
    diceFaceKeyList = []
    for x in message_content.split():
        for i in list:
            if x == i:
                diceFaceValueList.append(list[x])
                diceFaceKeyList.append(i)
                
        try:
            diceNumberList.append(int(x))
            
        except:
            continue

    if len(diceFaceValueList) == 1:
        if len(diceNumberList) == 1:
            resultList.append(DiceRoll(diceNumberList[0], diceFaceValueList[0], diceFaceKeyList[0], messageAuthor))
    elif len(diceFaceValueList) > 1:
        for f in diceFaceValueList:
            if len(diceNumberList) == 1:
                 resultList.append(DiceRoll(diceNumberList[0],f, diceFaceKeyList[0], messageAuthor))
            elif len(diceNumberList) > 1:
                resultList.append(DiceRoll(diceNumberList[diceFaceValueList.index(f)], f, diceFaceKeyList[diceFaceValueList.index(f)], messageAuthor))
    for h in resultList:
        resultString += h + "\n"
    return resultString

def Attacking():
    i = 0
    resultRandom = random.randrange(1,len(listAuthor))
    for x in listAuthor:
        if i == resultRandom:
            armorDice = random.randrange(1,21)
            print(f"{armorDice} hacia {listAuthor[x]}")
            if calcDictionary[listAuthor[x]] <= armorDice:
                return f"Se atacara a {listAuthor[x]} con un: {armorDice}"
            else:
                return "No se pudo atacar"
        else:
            i += 1

def AttackingM():
    i = 0
    resultRandom = random.randrange(1,len(listAuthor))
    for x in listAuthor:
        if i == resultRandom:
            armorDice = random.randrange(17,21)
            print(armorDice)
            if calcDictionary[listAuthor[x]] <= armorDice:
                return f"Se atacara a {listAuthor[x]} con un: {armorDice}"
        else:
            i += 1

def AdvantageDisadvantageCalc(message_content,messageAuthor):
    nick = AuthorChangeName(messageAuthor)
    dice1 = random.randrange(1,21)
    dice2 = random.randrange(1,21)
    messageCommand = message_content.split()
    print(f" Resultado de tirar en {messageCommand[0].replace("!", "")} Tirada1: {dice1}, Tirada2: {dice2}")
    match messageCommand[0]:
        case "!advantage":
            if dice1 >= dice2:
                return f"Tirada en ventaja por {nick}, resultado: {dice1}"
            else:
                return f"Tirada en ventaja por {nick}, resultado: {dice2}"
        
        case "!disadvantage":
            if dice1 <= dice2:
                return f"Tirada en desventaja por {nick}, resultado: {dice1}"
            else:
                return f"Tirada en desventaja por {nick}, resultado: {dice2}"
            
def ViewHealth(message_content,messageAuthor):
    messageCommand = message_content.split()
    messageAction = messageCommand[0].replace("!", "")
    nick = AuthorChangeName(messageAuthor)
    concatstring = ""
    if messageAction == "me":
        for x in healthDictionary:
            if nick == x:
                print(f"{nick}: {healthDictionary[x]} HP")
                return f"{nick}: {healthDictionary[x]} HP"
    elif messageAction == "health":
        for x in healthDictionary:
            concatstring = concatstring +  f"{x}: {healthDictionary[x]} HP \n"
            print(concatstring)
        print("final: " + concatstring)
        return concatstring

def HealthModifier(message_content,messageAuthor):
    messageCommand = message_content.split()
    messageAction = messageCommand[0].replace("!", "")
    nick = AuthorChangeName(messageAuthor)
    operationResult = 0
    if messageAction == "add":
        for x in healthDictionary:
            if len(messageCommand) == 3 and messageCommand[2].capitalize() in healthDictionary.keys():
                keyChecker = messageCommand[2].capitalize()
                operationResult = healthDictionary[keyChecker] + abs(int(messageCommand[1]))
                if operationResult > healthDictionaryReset[keyChecker]:
                    healthDictionary[keyChecker] = healthDictionaryReset[keyChecker]
                else:
                    healthDictionary[keyChecker] = operationResult
                print(f"{keyChecker}: {healthDictionary[keyChecker]} HP")
                return f"{keyChecker}: {healthDictionary[keyChecker]} HP"
            if nick == x:
                operationResult = healthDictionary[x] + abs(int(messageCommand[1]))
                if operationResult > healthDictionaryReset[x]:
                    healthDictionary[x] = healthDictionaryReset[x]
                else:
                    healthDictionary[x] = operationResult
                print(f"{nick}: {healthDictionary[x]} HP")
                return f"{nick}: {healthDictionary[x]} HP"
    elif messageAction == "minus":
        for x in healthDictionary:
            if nick == x:
                operationResult = healthDictionary[x] - abs(int(messageCommand[1]))
                if operationResult < 0 :
                    operationResult = 0
                healthDictionary[x] = operationResult
                print(f"{nick}: {healthDictionary[x]} HP")
                return f"{nick}: {healthDictionary[x]} HP"
    elif messageAction == "reset":
        for x in healthDictionary:
                healthDictionary[x] = healthDictionaryReset[x]
                print(f"{x}: {healthDictionary[x]} HP")
        return f"HP restaurado a todos"

###### Codigo para mandar fotos #######
def PhotoSending(message_content):
    directory = os.getenv('PHOTOSDIR')
    imageName = message_content.split()
    fileNameConcat = ""

    match imageName[2]:
        case "png":
            fileNameConcat = imageName[1] + ".png"
        case "jpeg":
            fileNameConcat = imageName[1] + ".jpeg"
        case "jpg":
            fileNameConcat = imageName[1] + ".jpg"
            return fileNameConcat
        case "webp":
            fileNameConcat = imageName[1] + ".webp"

    embed = discord.Embed()

    file = discord.File(f"{directory}\\{fileNameConcat}", filename=fileNameConcat)
    embed.set_image(url=f"attachment://{fileNameConcat}")
    return (file, embed)

def Initiative():
    res = ""
    for x in initiativeDictionary:   
        dice = DiceRoll(1,20,"d20",x)
        diceSplit = dice.split()
        arrayRes = NumberParser(diceSplit)
        totalRes = int(arrayRes) + initiativeDictionary[x]
        res += f"{x} ha sacado un {totalRes} de iniciativa \n"
    return res

def SurpriseIni():
    res = ""
    for x in initiativeDictionary:   
        dice1 = random.randrange(1,21)
        dice2 = random.randrange(1,21)
        print(f" Resultado Tirada1: {dice1}, Tirada2: {dice2}")
        if dice1 <= dice2:
            res += f"{x} ha sacado un { dice1 + initiativeDictionary[x]} de iniciativa \n"
        else:
            res += f"{x} ha sacado un { dice2 + initiativeDictionary[x]} de iniciativa \n"
        print(res)
    return res

def NewDiceRoller(message_content,messageAuthor):
    messageCommand = message_content.split()
    messageAction = messageCommand[0].replace("!", "")
    res = ""
    match messageAction:

        case "d4":
            if len(messageCommand) == 1:
                res = DiceRoll(1, 4, "d4", messageAuthor)
            elif len(messageCommand) == 2:
                if messageCommand[1].startswith("+"):
                    plus = int(messageCommand[1].replace("+",""))
                    res = DiceRoll(1, 4, "d4", messageAuthor)
                    diceSplit = res.split()
                    arrayRes = NumberParser(diceSplit)
                    totalRes = int(arrayRes) + plus
                    res = res.replace(str(arrayRes), str(totalRes))
                else:
                    res = DiceRoll(int(messageCommand[1]), 4, "d4", messageAuthor)
            elif len(messageCommand) == 3:
                res = DiceRoll(int(messageCommand[1]), 4, "d4", messageAuthor)
                plus = int(messageCommand[2].replace("+",""))
                diceSplit = res.split()
                arrayRes = NumberParser(diceSplit)
                totalRes = int(arrayRes) + plus
                res = res.replace(str(arrayRes), str(totalRes))

        case "d6":
            if len(messageCommand) == 1:
                res = DiceRoll(1, 6, "d6", messageAuthor)
            elif len(messageCommand) == 2:
                if messageCommand[1].startswith("+"):
                    plus = int(messageCommand[1].replace("+",""))
                    res = DiceRoll(1, 6, "d6", messageAuthor)
                    diceSplit = res.split()
                    arrayRes = NumberParser(diceSplit)
                    totalRes = int(arrayRes) + plus
                    res = res.replace(str(arrayRes), str(totalRes))
                else:
                    res = DiceRoll(int(messageCommand[1]), 6, "d6", messageAuthor)
            elif len(messageCommand) == 3:
                res = DiceRoll(int(messageCommand[1]), 6, "d6", messageAuthor)
                plus = int(messageCommand[2].replace("+",""))
                diceSplit = res.split()
                arrayRes = NumberParser(diceSplit)
                totalRes = int(arrayRes) + plus
                res = res.replace(str(arrayRes), str(totalRes))

        case "d8":
            if len(messageCommand) == 1:
                res = DiceRoll(1, 8, "d8", messageAuthor)
            elif len(messageCommand) == 2:
                if messageCommand[1].startswith("+"):
                    plus = int(messageCommand[1].replace("+",""))
                    res = DiceRoll(1, 8, "d8", messageAuthor)
                    diceSplit = res.split()
                    arrayRes = NumberParser(diceSplit)
                    totalRes = int(arrayRes) + plus
                    res = res.replace(str(arrayRes), str(totalRes))
                else:
                    res = DiceRoll(int(messageCommand[1]), 8, "d8", messageAuthor)
            elif len(messageCommand) == 3:
                res = DiceRoll(int(messageCommand[1]), 8, "d8", messageAuthor)
                plus = int(messageCommand[2].replace("+",""))
                diceSplit = res.split()
                arrayRes = NumberParser(diceSplit)
                totalRes = int(arrayRes) + plus
                res = res.replace(str(arrayRes), str(totalRes))

        case "d10":
            if len(messageCommand) == 1:
                res = DiceRoll(1, 10, "d10", messageAuthor)
            elif len(messageCommand) == 2:
                if messageCommand[1].startswith("+"):
                    plus = int(messageCommand[1].replace("+",""))
                    res = DiceRoll(1, 10, "d10", messageAuthor)
                    diceSplit = res.split()
                    arrayRes = NumberParser(diceSplit)
                    totalRes = int(arrayRes) + plus
                    res = res.replace(str(arrayRes), str(totalRes))
                else:
                    res = DiceRoll(int(messageCommand[1]), 10, "d10", messageAuthor)
            elif len(messageCommand) == 3:
                res = DiceRoll(int(messageCommand[1]), 10, "d10", messageAuthor)
                plus = int(messageCommand[2].replace("+",""))
                diceSplit = res.split()
                arrayRes = NumberParser(diceSplit)
                totalRes = int(arrayRes) + plus
                res = res.replace(str(arrayRes), str(totalRes))

        case "d12":
            if len(messageCommand) == 1:
                res = DiceRoll(1, 12, "d12", messageAuthor)
            elif len(messageCommand) == 2:
                if messageCommand[1].startswith("+"):
                    plus = int(messageCommand[1].replace("+",""))
                    res = DiceRoll(1, 12, "d12", messageAuthor)
                    diceSplit = res.split()
                    arrayRes = NumberParser(diceSplit)
                    totalRes = int(arrayRes) + plus
                    res = res.replace(str(arrayRes), str(totalRes))
                else:
                    res = DiceRoll(int(messageCommand[1]), 12, "d12", messageAuthor)
            elif len(messageCommand) == 3:
                res = DiceRoll(int(messageCommand[1]), 12, "d12", messageAuthor)
                plus = int(messageCommand[2].replace("+",""))
                diceSplit = res.split()
                arrayRes = NumberParser(diceSplit)
                totalRes = int(arrayRes) + plus
                res = res.replace(str(arrayRes), str(totalRes)) 

        case "d20":
            if len(messageCommand) == 1:
                res = DiceRoll(1, 20, "d20", messageAuthor)
            elif len(messageCommand) == 2:
                if messageCommand[1].startswith("+"):
                    plus = int(messageCommand[1].replace("+",""))
                    res = DiceRoll(1, 20, "d20", messageAuthor)
                    diceSplit = res.split()
                    arrayRes = NumberParser(diceSplit)
                    totalRes = int(arrayRes) + plus
                    res = res.replace(str(arrayRes), str(totalRes))
                else:
                    res = DiceRoll(int(messageCommand[1]), 20, "d20", messageAuthor)
            elif len(messageCommand) == 3:
                res = DiceRoll(int(messageCommand[1]), 20, "d20", messageAuthor)
                plus = int(messageCommand[2].replace("+",""))
                diceSplit = res.split()
                arrayRes = NumberParser(diceSplit)
                totalRes = int(arrayRes) + plus
                res = res.replace(str(arrayRes), str(totalRes))

        case "d100":
             if len(messageCommand) == 1:
                res = DiceRoll(1, 100, "d100", messageAuthor)
             elif len(messageCommand) == 2:
                if messageCommand[1].startswith("+"):
                    plus = int(messageCommand[1].replace("+",""))
                    res = DiceRoll(1, 100, "d100", messageAuthor)
                    diceSplit = res.split()
                    arrayRes = NumberParser(diceSplit)
                    totalRes = int(arrayRes) + plus
                    res = res.replace(str(arrayRes), str(totalRes))
                else:
                    res = DiceRoll(int(messageCommand[1]), 100, "d100", messageAuthor)
             elif len(messageCommand) == 3:
                res = DiceRoll(int(messageCommand[1]), 100, "d100", messageAuthor)
                plus = int(messageCommand[2].replace("+",""))
                diceSplit = res.split()
                arrayRes = NumberParser(diceSplit)
                totalRes = int(arrayRes) + plus
                res = res.replace(str(arrayRes), str(totalRes))

    return res

def NumberParser(text):
    resText = ""
    for x in text:
        try:
            int(x)
            resText = x
        except:
                continue
    return resText


# def DiceRoll(diceNumber, diceFaceValue, diceFaceKey, messageAuthor):
#     result = 0
#     nick = AuthorChangeName(messageAuthor)
#     print(f"Tirada de un {diceFaceKey} por {nick}")
#     for x in range(diceNumber):
#         resultRandom = random.randrange(1,diceFaceValue + 1)
#         result += resultRandom
#         print(f"tirada {x + 1} : {resultRandom}")
#     if diceNumber == 1:
#         if result == 20:

#             return f"Tirada de un {diceFaceKey}, NAT 20 tu turno de brillar {nick}"
        
#         return f"Tirada de un {diceFaceKey} por {nick}, resultado: {result}"
#     else:
#         return f"Tirada de un {diceFaceKey} por {nick}, resultado total: {result}"




