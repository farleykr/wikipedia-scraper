from bs4 import BeautifulSoup
import requests
import re


with open('music_list.txt', 'a') as doc:

    to_exclude = ['1', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', '11', '12',
                  '13', '14', '15', '16', '17', '18', 
                  '19', '20', '21', '22', '23', '24',
                  '25', '26', '27', '28', '29', '30',
                  '31', '-', 'N/A'] 
    
    to_exclude_mos = ['January', 'February', 'March', 'April', 
                      'May', 'June', 'July', 'August', 
                      'September', 'October', 'November', 'December']

    for year in range(1970, 1980):
        source = requests.get(
            f'https://en.wikipedia.org/wiki/{year}_in_music').text
        soup = BeautifulSoup(source, 'lxml')

        album_tables = soup.find_all('table', class_="wikitable")

        for album_table in album_tables[:12]:
            album_rows = album_table.find_all('tr')

            for row in album_rows[1:]:
                cells = row.find_all('td')
                
                if cells[0].text.strip() in to_exclude:
                    
                    album = cells[1].text
                    band = cells[2].text
                    
                    doc.write(f'{album} by {band} ({year})\n')

                
                else:
                    album = cells[0].text
                    band = cells[1].text
                    
                    doc.write(f'{album} by {band} ({year})\n')


    for year in range(1980, 2004):
        source = requests.get(
            f'https://en.wikipedia.org/wiki/{year}_in_music').text
        
        soup = BeautifulSoup(source, 'lxml')
        
        album_tables = soup.find_all('table', class_="wikitable")

        for album_table in album_tables[:4]:
            album_rows = album_table.find_all('tr')

            for row in album_rows[1:]:
                
                cells = row.find_all('td')

                try:
                    if cells[0].text.strip() in to_exclude:
                        
                        album = cells[1].text.strip()
                        band = cells[2].text.strip()
                    
                        doc.write(f'{album} by {band} ({year})\n')

                    elif cells[1].text.strip() in to_exclude:
                        
                        album = cells[2].text.strip()
                        band = cells[3].text.strip()
                    
                        doc.write(f'{album} by {band} ({year})\n')
                
                    else:
                        album = cells[0].text.strip()
                        band = cells[1].text.strip()
                    
                        doc.write(f'{album} by {band} ({year})\n')
                    
                except IndexError:
                    pass


    source = requests.get(
        f'https://en.wikipedia.org/wiki/2004_in_music').text

    soup = BeautifulSoup(source, 'lxml')

    album_tables = soup.find_all('table', class_="wikitable")

    for album_table in album_tables[1:5]:
        album_rows = album_table.find_all('tr')

        for row in album_rows[1:]:
            
            cells = row.find_all('td')

            try:
                if cells[0].text.strip() in to_exclude:
                    
                    album = cells[1].text.strip()
                    band = cells[2].text.strip()
                
                    doc.write(f'{album} by {band} (2004)\n')

                elif cells[1].text.strip() in to_exclude:
                    
                    album = cells[2].text.strip()
                    band = cells[3].text.strip()
                
                    doc.write(f'{album} by {band} (2004)\n')
            
                else:
                    album = cells[0].text.strip()
                    band = cells[1].text.strip()
                
                    doc.write(f'{album} by {band} (2004)\n')
                
            except IndexError:
                pass

    for year in range(2005, 2019):
        src = requests.get(
            f'https://en.wikipedia.org/wiki/List_of_{year}_albums').text
        soup = BeautifulSoup(src, 'lxml')
        album_tables = soup.find_all('table', class_="wikitable")

        for album_table in album_tables:
            album_rows = album_table.find_all('tr')

            for row in album_rows[1:]:
                cells = row.find_all('td')

                try:
                    if re.sub('\d+', '', cells[0].text.strip()) in to_exclude_mos:
                        album = cells[2].text.strip()
                        band = cells[1].text.strip()
                    
                        doc.write(f'{album} by {band} ({year})\n')
                
                    else:
                        album = cells[1].text.strip()
                        band = cells[0].text.strip()
                    
                        doc.write(f'{album} by {band} ({year})\n')

                except IndexError:
                    pass

    src = requests.get(
        f'https://en.wikipedia.org/wiki/List_of_2019_albums').text
    soup = BeautifulSoup(src, 'lxml')
    album_tables = soup.find_all('table', class_="wikitable")

    for album_table in album_tables:
        album_rows = album_table.find_all('tr')

        for row in album_rows[1:]:
            cells = row.find_all('td')

            try:
                if re.sub('\d+', '', cells[0].text.strip()) in to_exclude_mos:
                    album = cells[2].text.strip()
                    band = cells[1].text.strip()
                
                    doc.write(f'{album} by {band} (2019)\n')
            
                else:
                    album = cells[1].text.strip()
                    band = cells[0].text.strip()
                
                    doc.write(f'{album} by {band} (2019)\n')

            except IndexError:
                pass
