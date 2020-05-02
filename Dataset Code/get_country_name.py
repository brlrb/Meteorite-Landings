import csv
import requests
import json
import pandas as pd


def raw_lat_lng():
    print("**** raw_lat_lng ****")
    with open("unknown_country5.csv") as csv_file:
        read_csv = csv.reader(csv_file, delimiter = ',')
        next(read_csv, None)
        list_country_name = []
        tracker = 0
        for row in read_csv:
            tracker = tracker + 1
            print("tracker: ", tracker)
            api_call_url = "http://api.geonames.org/countryCodeJSON?lat=" + row[3] + "&lng=" + row[4] + "&username=<API_KEY>2"
            print("Results: ", api_call_url, '\n')
            results = requests.get(api_call_url)
            results = results.text
            json_results = json.loads(results)

            print("Results: ", json_results, '\n')


            if('countryName' in json_results):
                print("***** COUNTRY YES ***** ", json_results["countryName"])

                list_country_name.append({
                    "latitude" : float(row[3]),
                    "longitude" : float(row[4]),
                    "country" : json_results["countryName"],
                    "country_code" : json_results["countryCode"],
                    "distnce" : 0,
                    "location_type" : "land"
                })

            else:
                
                print("***** COUNTRY NO ***** ")

                api_call_url = "http://api.geonames.org/oceanJSON?formatted=true&lat=" + row[3] + "&lng=" + row[4] + "&username=<API_KEY>&style=full"
                print("Results: ", api_call_url, '\n')
                results = requests.get(api_call_url)
                # print("Results: ", results, '\n')
                results = results.text
                json_results = json.loads(results)
                
                if('ocean' in json_results):
                    print("***** OCEAN YES ***** ")

                    list_country_name.append({
                        "latitude" : float(row[3]),
                        "longitude" : float(row[4]),
                        "country" : json_results["ocean"]["name"],
                        "country_code" : "Unknown",
                        "distnce" : json_results["ocean"]["distance"],
                        "location_type" : "ocean"
                    })

                else:

                    print("***** NOTHING ***** ")

                    list_country_name.append({

                        "latitude" : float(row[3]),
                        "longitude" : float(row[4]),
                        "country" : "Unknown",
                        "country_code" : "Unknown",
                        "distnce" : 0,
                        "location_type" : "Unknown"
                    })


                
        print("list_country_name + code: ", list_country_name , '\n')

        create_json_name = open("JSONcountry_name3.json","w+") 
        create_json_name.write(str(list_country_name))

        create_json_name.close() 


def ocean_name():
    with open("unknown_country3.csv") as csv_file:
        read_csv = csv.reader(csv_file, delimiter = ',')
        next(read_csv, None)
        list_country_name = []
        tracker = 0
        for row in read_csv:
            tracker = tracker + 1
            print("tracker: ", tracker)
            api_call_url = "http://api.geonames.org/oceanJSON?formatted=true&lat=" + row[3] + "&lng=" + row[4] + "&username=<API_KEY>2&style=full"
            print("Results: ", api_call_url, '\n')
            results = requests.get(api_call_url)
            # print("Results: ", results, '\n')
            results = results.text
            json_results = json.loads(results)
            # print("json_results: ", json_results , '\n')


            if('ocean' in json_results):
                print("***** OCEAN YES ***** ", json_results["ocean"]["name"])

                list_country_name.append({
                    "latitude" : float(row[3]),
                    "longitude" : float(row[4]),
                    "country" : json_results["ocean"]["name"],
                    "country_code" : "Unknown",
                    "distnce" : json_results["ocean"]["distance"],
                    "location_type" : "Ocean"
                })

            else:
                api_call_url = "http://api.geonames.org/countryCodeJSON?lat=" + row[3] + "&lng=" + row[4] + "&username=<API_KEY>"
                print("Results: ", api_call_url, '\n')
                results = requests.get(api_call_url)
                # print("Results: ", results, '\n')
                results = results.text
                json_results = json.loads(results)
                
                if('countryName' in json_results):
                    print("***** COUNTRY YES ***** ", json_results["countryName"])

                    list_country_name.append({
                        "latitude" : float(row[3]),
                        "longitude" : float(row[4]),
                        "country" : json_results["countryName"],
                        "country_code" : json_results["countryCode"]
                    })

                else:
                    
                    print("***** NOTHING ***** ")

                    list_country_name.append({

                        "latitude" : float(row[3]),
                        "longitude" : float(row[4]),                
                        "country" : "Unknown",
                        "country_code" : "Unknown"
                    })



                
        print("list ocean + code: ", list_country_name , '\n')

        create_json_name = open("JSONocean_name3.json","w+") 
        create_json_name.write(str(list_country_name))

        create_json_name.close() 



def country_name_nearby():
    with open("unonowncountry_csv.csv") as csv_file:
        read_csv = csv.reader(csv_file, delimiter = ',')
        next(read_csv, None)
        list_country_name = []
        tracker = 0
        for row in read_csv:
            tracker = tracker + 1
            print("tracker: ", tracker)
            # http://api.geonames.org/findNearbyPlaceNameJSON?lat=47.3&lng=9&username=<API_KEY>2
            api_call_url = "http://api.geonames.org/findNearbyPlaceNameJSON?lat=" + row[2] + "&lng=" + row[3] + "&username=<API_KEY>2"
            print("Results: ", api_call_url, '\n')
            results = requests.get(api_call_url)
            # print("Results: ", results, '\n')
            results = results.text
            json_results = json.loads(results)
            json_results = json_results["geonames"]
            # print("json_results: ", json_results , '\n')


            if(not len(json_results) == 0):
                print("***** YES *****")
                list_country_name.append({
                    "latitude" : float(row[2]),
                    "longitude" : float(row[3]),
                    "country" : json_results[0]["countryName"],
                    "distance" : json_results[0]["distance"],
                    "countryCode" : json_results[0]["countryCode"],
                    "location_type" : "NearbyPlaceName"
                })

            else:
                print("***** NO **** ")
                list_country_name.append({
                    "latitude" : (row[2]),
                    "longitude" : (row[3]),
                    "country" : "Unknown",
                    "distnce" : "Unknown",
                    "countryCode" : "Unknown",
                    "location_type" : "Unknown"              
                })


                
        print("list nearby place + code: ", list_country_name , '\n')

        create_json_name = open("JSONnearby_place_name.json","w+") 
        create_json_name.write(str(list_country_name))

        create_json_name.close() 




def csv_to_json():

    df = pd.read_json (r'JSONcountry_name3.json')
    df.to_csv (r'5_CSVcountry_name.csv', index = None)




##############################
###### CALL FUNCTION #########

# raw_lat_lng()
# ocean_name()
# country_name_nearby()
csv_to_json()










    # http://api.geonames.org/findNearbyPlaceNameJSON?lat=50.77500&lng=6.08333&username=<API_KEY>