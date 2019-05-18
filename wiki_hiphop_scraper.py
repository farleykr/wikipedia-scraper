from bs4 import BeautifulSoup
import requests
import re

with open('hiphop_music_list.txt', 'a') as doc:
    months = ['January', 'February', 'March', 'April', 
            'May', 'June', 'July', 'August', 
            'September', 'October', 'November', 'December',
            'Unknown']

    to_exclude = ['1', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', '11', '12',
                  '13', '14', '15', '16', '17', '18', 
                  '19', '20', '21', '22', '23', '24',
                  '25', '26', '27', '28', '29', '30',
                  '31', '-', 'N/A'] 

    for year in range(1980, 2017):
        src = requests.get(
            f'https://en.wikipedia.org/wiki/{year}_in_hip_hop_music').text
        soup = BeautifulSoup(src, 'lxml')
        album_table = soup.find('table', class_="wikitable")

        album_rows = album_table.find_all('tr')

        try:
            for row in album_rows[1:]:

                cells = row.find_all('td')

                if re.sub('\d+', '', cells[0].text.strip()).strip() in months:
                    album = cells[2].text.strip()
                    band = cells[1].text.strip()

                    doc.write(f'{album} by {band} ({year})\n')
                
                else:
                    album = cells[1].text.strip()
                    band = cells[0].text.strip()

                    doc.write(f'{album} by {band} ({year})\n')
        
        except IndexError:
            pass
    
    for year in range(2017, 2019):
        src = requests.get(
            f'https://en.wikipedia.org/wiki/{year}_in_hip_hop_music').text
        soup = BeautifulSoup(src, 'lxml')
        album_tables = soup.find_all('table', class_="wikitable")

        for album_table in album_tables[:12]:
            album_rows = album_table.find_all('tr')

            try:
                for row in album_rows[1:]:

                    cells = row.find_all('td')

                    if cells[0].text.strip() in to_exclude:
                        album = cells[2].text.strip()
                        band = cells[1].text.strip()

                        doc.write(f'{album} by {band} ({year})\n')
                    
                    else:
                        album = cells[1].text.strip()
                        band = cells[0].text.strip()

                        doc.write(f'{album} by {band} ({year})\n')
            
            except IndexError:
                pass

    for year in range(2019, 2020):
        src = requests.get(
            f'https://en.wikipedia.org/wiki/{year}_in_hip_hop_music').text
        soup = BeautifulSoup(src, 'lxml')
        album_tables = soup.find_all('table', class_="wikitable")

        for album_table in album_tables[:2]:
            album_rows = album_table.find_all('tr')

            try:
                for row in album_rows[1:]:

                    cells = row.find_all('td')

                    if cells[0].text.strip() in to_exclude:
                        album = cells[2].text.strip()
                        band = cells[1].text.strip()

                        doc.write(f'{album} by {band} ({year}\n)')
                    
                    else:
                        album = cells[1].text.strip()
                        band = cells[0].text.strip()

                        doc.write(f'{album} by {band} ({year}\n)')
            
            except IndexError:
                pass