import csv
import geocoder
from tqdm import tqdm

outfile = open("withgeocode.csv","w")

with open(r"C:\Users\levi3\OneDrive\Documents\DataChallenge_SayariAnalytics\csv_bahamas_leaks.2017-12-19\bahamas_leaks.nodes.address.csv","r") as csvfile:
    filer = csv.DictReader(csvfile)
    outfieldnames = filer.fieldnames.append("geocode")
    print(filer.fieldnames)
    writer = csv.DictWriter(outfile,fieldnames = filer.fieldnames)
    writer.writeheader()
    for each in tqdm(filer):
        g = geocoder.google(each["address"]) 
        each["geocode"] = g.latlng 
        writer.writerow(each)

