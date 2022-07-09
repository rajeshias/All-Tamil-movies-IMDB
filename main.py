import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

wait = WebDriverWait(driver, 200)

movieList = []
for i in range(1, 6400, 50):
    driver.get(f"https://www.imdb.com/search/title/?title_type=feature&primary_language=ta&start={i}")

    listMovies = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3[@class='lister-item-header']/a")))
    movieYear = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='lister-item-year text-muted unbold']")))
    for movie, year in zip(listMovies, movieYear):
        movieList.append({
            "label": movie.text,
            "year": year.text.split(" ")[-1].replace("(","").replace(")","")
        })


# Serializing json 
json_object = json.dumps(movieList, indent = 4)
  
# Writing to sample.json
with open("tamilMovies.json", "w") as outfile:
    outfile.write(json_object)