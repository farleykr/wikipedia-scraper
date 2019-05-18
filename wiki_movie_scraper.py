from bs4 import BeautifulSoup
import requests



with open('movie_list.txt', 'a') as doc:

    to_exclude = ['1', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', '11', '12',
              '13', '14', '15', '16', '17', '18', 
              '19', '20', '21', '22', '23', '24',
              '25', '26', '27', '28', '29', '30',
              '31', '-', 'N/A', '?']

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 
                'G', 'H', 'I', 'J', 'K', 'L', 
                'M', 'N', 'O', 'P', 'Q', 'R', 
                'S', 'T', 'U', 'V', 'W', 'X', 
                'Y', 'Z', '‡']

    for year in range(1970, 2004):
        src = requests.get(
            f'https://en.wikipedia.org/wiki/{year}_in_film').text
        soup = BeautifulSoup(src, 'lxml')

        for letter in alphabet:
            try:
                p_tag = soup.find('b', text=f'{letter}').parent
                
                movie_list = p_tag.findNext('ul')

                movies = movie_list.find_all('li')

                for movie in movies:
                    doc.write(f'{movie.a.text} ({year})\n')

            except:
                pass 


    for year in range(2004, 2020):
        src = requests.get(
            f'https://en.wikipedia.org/wiki/{year}_in_film').text
        soup = BeautifulSoup(src, 'lxml')
        movie_tables = soup.find_all('table', class_="wikitable")

        if year == 2010:
            for table in movie_tables[-4:]:
                movie_rows = table.find_all('tr')

                for row in movie_rows[1:]:
                    cells = row.find_all('td')

                    try:
                        if cells[0].text.strip() in alphabet:
                            movie = cells[1].text.strip()
                        
                            doc.write(f'{movie} ({year})\n')

                        elif cells[1].text.strip() in alphabet:
                            movie = cells[2].text.strip()
                        
                            doc.write(f'{movie} ({year})\n')
                
                        else:
                            movie = cells[0].text.strip()
                        
                            doc.write(f'{movie} ({year})\n')

                    except IndexError:
                        pass

        else:

            for table in movie_tables[-4:]:
                movie_rows = table.find_all('tr')

                for row in movie_rows[1:]:
                    cells = row.find_all('td')

                    try:
                        if cells[0].text.strip() in to_exclude:
                            movie = cells[1].text.strip()
                        
                            doc.write(f'{movie} ({year})\n')
                    
                        else:
                            movie = cells[0].text.strip()
                        
                            doc.write(f'{movie} ({year})\n')

                    except IndexError:
                        pass
