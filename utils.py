import requests
from bs4 import BeautifulSoup
import time
from datetime import date

# list of items to check for
star_wars_skins = ['212th Battalion Trooper', 
                   '501st Trooper', 
                   'Ahsoka Tano', 
                   "Ahsoka's Clone Trooper", 
                   "Anakin Skywalker", 
                   "Boba Fett", 
                   "Clone Trooper", 
                   "Coruscant Guard", 
                   "Darth Maul", "Darth Vader", 
                   "Fennec Shand", 
                   "Finn", 
                   "Han Solo", 
                   "Imperial Stormtrooper", 
                   "Krrsantan", 
                   "Kylo Ren", 
                   "Leia Organa", 
                   "Luke Skywalker", 
                   "Mandalorian", 
                   "Obi-Wan Kenobi", 
                   "Padmé Amidala", 
                   "Rey", 
                   "Sith Trooper",
                   "Wolf Pack Trooper", 
                   "Zorii Bliss"]


def skins_result(url):
    # initiates skin_found as FALSE, later changing to TRUE if skin is found
    skin_found = False

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    session = requests.Session()
    
    try:
        # gets a response from the website
        response = session.get(url, headers=headers)
        
        # print('HTML Status Code: ', response.status_code)

        # checks for valid connection
        if response.status_code == 200:
            # gets HTML of site
            soup = BeautifulSoup(response.text,'html.parser')

            # today's date
            today = date.today()

            # finds all skin titles
            skins = soup.find_all('h3')
            # finds skin prices in VC
            prices = soup.find_all('p', id='pricep')
            

            # creates an empty list to house skin and price
            skin_price_pairs = []
            print(f"Date: {today}")
            print("SKIN | PRICE (V BUCKS)")
            print("----------------------")

            # fills skin_price_pairs with skin + price 
            for skin, price in zip(skins,prices):
                skin_result = skin.text.strip()
                price_result = price.text.strip()

                skin_price_pairs.append((skin_result, price_result))

            # prints out each skin + price from the previous created list, also checks each skin against the star_wars_skins list
            for skin, price in skin_price_pairs:
                print(f'{skin}: {price} VC')
                if skin in star_wars_skins:
                     skin_found = True
                     print("STAR WARS SKIN FOUND")
            
            # gives the verdict
            if skin_found:
                print("There is at least one Star Wars related item in today's shop.")
            else:
                print("\nNo luck, try again tomrrow.")

        # issue with connection if non 200 status code
        else:
            print('check connection / html')
    
    except Exception as e:
        return f'An error occured {e}'
    finally:
        session.close()


