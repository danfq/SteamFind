#SteamFind v1.0.0 - Utilities
#DanFQ

#Requirements
import codecs
import datetime
import requests
from colorama import Fore
from bs4 import BeautifulSoup
import pyfiglet
import os

class Util():

    steamAppURL = "https://store.steampowered.com/app/"

    #Success List
    successList = ["\n-- " + str(datetime.date.today()) + " | " + str(datetime.datetime.now().strftime("%H:%M:%S")) + " --\n\n"]

    #Banner
    def steamFindBanner():
        print(Fore.LIGHTGREEN_EX + pyfiglet.figlet_format("SteamFind"))
        print(" A Steam AppID Resolver Utility\n")
        print(" - by DanFQ - \n\n")

    #Functions
    def mainMenu():
        print(Fore.LIGHTYELLOW_EX + "\n\n-- Main Menu --\n")
        print(Fore.CYAN + "\n [ID] Search from a Start AppID to a Final AppID (can be very slow)")
        print(Fore.CYAN + "\n [SID] Search for specific AppID (fastest)")
        print(Fore.CYAN + "\n [Q] Search by Query (BETA)")
        print(Fore.CYAN + "\n [GUI] Launch GUI Mode (BETA)")
        menu_choice = input(Fore.CYAN + "\n\n [*] Choose a Search Mode: ").lower().strip()
        try:
            if menu_choice == "id":
                Util.requestRange()
            elif menu_choice == "q":
                Util.queryFinder()
            elif menu_choice == "sid":
                os.system("cls")
                Util.steamFindBanner()
                Util.specificID()
            elif menu_choice == "gui":
                os.system("cls")
                Util.steamFindBanner()
                Util.launchGUI()
            else:
                print('Invalid Input')
                return Util.mainMenu()
        except Exception as error:
            print("Please enter a valid option. | " + str(error))
            return Util.mainMenu()

    def backToMenu():
        go_back = str(input(Fore.CYAN + "\n\n [*] Go back to the Main Menu? (Y/N): ")).lower().strip()
        try:
            if go_back[0] == "y":
                os.system("cls")
                Util.steamFindBanner()
                Util.mainMenu()
            elif go_back[0] == "n":
                print("\n")
                return False
            else:
                print('Invalid Input')
                return Util.backToMenu()
        except Exception as error:
            print("Please enter Y or N. | " + str(error))
            return Util.backToMenu()

    def addToSuccessList(pageURL, pageTitle):
        Util.successList.append("'" + str(pageTitle) + "' | " + str(pageURL + "\n\n"))


    def saveSuccess():

        success_file = codecs.open("success.txt", "a", encoding="utf-8")

        for item in Util.successList:
            success_file.write(item)

        success_file.close()

        print(Fore.LIGHTBLUE_EX + "\n [+] Successful Results saved to '" + Fore.GREEN + "success.txt" + Fore.LIGHTBLUE_EX + "'.\n\n")


    def checkSave():
        check = str(input(Fore.CYAN + "\n\n [*] Would you like to save your successful results? (Y/N): ")).lower().strip()
        try:
            if check[0] == "y":
                Util.saveSuccess()
            elif check[0] == "n":
                print("\n")
                return False
            else:
                print('Invalid Input')
                return Util.checkSave()
        except Exception as error:
            print("Please enter Y or N. | " + str(error))
            return Util.checkSave()


    def getTitle(response):
        soupData = BeautifulSoup(response.text, 'html.parser')
        for title in soupData.find_all('title'):
            pageTitle = title.get_text()

            if pageTitle == "Welcome to Steam":
                return Fore.YELLOW + "Redirected to Steam Homepage"
            else:
                Util.addToSuccessList(response.url, pageTitle.strip(" on Steam"))
                return Fore.GREEN + str(pageTitle).strip(" on Steam") + Fore.WHITE + " | " + response.url


    def checkURLs(urlList):
        for index, url in enumerate(urlList):
            try:
                response = requests.get(url)
                print(Fore.WHITE + "\n [" + str(index + 1) + "/" + str(len(urlList)) + "] Steam AppID: " + url.rsplit('/', 1)[-1] + " | " + Util.getTitle(response))
            except requests.ConnectionError:
                print(Fore.RED + "\n [-] URL is Not Valid | " + url)

        Util.checkSave()

    def queryFinder():
        print(Fore.YELLOW + " [*] This feature is not available yet.")
        Util.backToMenu()

    def queryLookup(query):
        print(Fore.YELLOW + " [*] This feature is not available yet.")
        Util.backToMenu()

    def createIDList(start, end):
        urlList = []

        for id in range(start, end + 1):
            urlList.append(Util.steamAppURL + str(id))

        print(Fore.MAGENTA + "\n [/] Generating URL List for IDs: " + Fore.GREEN + str(start) + " -> " + str(end) + Fore.WHITE + " | " + str(len(urlList)) + " Links\n")
        Util.checkURLs(urlList)


    def requestRange():
        os.system("cls")
        Util.steamFindBanner()
        print(Fore.LIGHTRED_EX + " Warning: Depending on the amount of IDs, this method can take a long time to complete.")
        print("\n\n")
        startID = input(Fore.CYAN + " [*] First AppID: ")
        endID = input(Fore.CYAN + " [*] Final AppID: ")
        os.system("cls")
        Util.steamFindBanner()
        Util.createIDList(int(startID), int(endID))

    def specificIDTitle(response):
        soupData = BeautifulSoup(response.text, 'html.parser')
        for title in soupData.find_all('title'):
            pageTitle = title.get_text()

            if pageTitle == "Welcome to Steam":
                return Fore.YELLOW + "Redirected to Steam Homepage"
            else:
                Util.addToSuccessList(response.url, pageTitle.strip(" on Steam"))
                return Fore.GREEN + str(pageTitle).strip(" on Steam") + Fore.WHITE + " | " + response.url

    def specificIDLookup(queryID):

        url = Util.steamAppURL + str(queryID)

        try:
            response = requests.get(url)
            print(Fore.WHITE + "\n Steam AppID: " + str(queryID) + " | " + Fore.YELLOW + "VALID ID" + Fore.WHITE + " | " + Util.getTitle(response) + "\n\n")
            Util.backToMenu()
        except requests.ConnectionError:
            print(Fore.RED + "\n [-] URL is Not Valid | " + url)

    def specificID():
        print("\n\n")
        query_id = input(Fore.CYAN + " [*] Steam AppID: ")
        os.system("cls")
        Util.steamFindBanner()
        Util.specificIDLookup(str(query_id))

    def launchGUI():
        print(Fore.YELLOW + " [*] This feature is not available yet.")
        Util.backToMenu()
