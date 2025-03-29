from django.shortcuts import render



def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')



import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

def scrape_flipkart_mobiles(request):
    product_name = []
    Price = []
    Description = []
    reviews_text = [] 

    for page in range(1, 6):  # Limiting to 5 pages for faster response
        url = f"https://www.flipkart.com/search?q=mobile+under+150000+rs&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        
        box = soup.find("div", class_="DOjaWF gdgoEp")
        if not box:
            continue  # Skip if the page structure is different

        names = box.find_all("div", class_="KzDlHZ")
        for i in names:
            product_name.append(i.text)

        prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
        for i in prices:
            Price.append(i.text)

        descriptions = box.find_all("ul", class_="G4BRas")
        for i in descriptions:
            Description.append(i.text)

        reviews = box.find_all("div", class_="_5OesEi")
        for i in reviews:
            reviews_text.append(i.text.strip())

    # Store data in a DataFrame
    df = pd.DataFrame({
        "Product Name": product_name,
        "Price": Price,
        "Description": Description,
        "Reviews": reviews_text
    })

    # Save to CSV (optional)
    # df.to_csv("flipkart_mobiles_under_150000.csv", index=False)

    # Return JSON response
    return JsonResponse(df.to_dict(orient="records"), safe=False)
