#import json
import demjson

def open_locations():
    # if locations does not exist, create it
    return demjson.decode_file("locations.json")

def open_links():
    # if locations does not exist, create it
    return demjson.decode_file("links.json")

def create_location(name, description, locations):
    locations.append({ 'name':name, 'description':description })
    json = demjson.encode(locations)
    print json

def create_link(location1, location2, direction, links):
    links.append({'loc1':location1, 'loc2':location2, 'direction':direction})
    json = demjson.encode(links)
    print links

def validate_links(links, locations):
    valid_locations = []
    for e in locations:
        valid_locations.append(e['name'])
    for f in links:
        if f['loc1'] or f['loc2'] not in valid_locations:
            for attribute, value in f.items():
                print('{} : {}'.format(attribute, value))

def validate_check_duplicates(locations):
    s = set([])
    duplicates = 0
    for g in locations:
        if g['name'] in s:
            duplicates += 1
        else:
            s.add(g['name'])
    print duplicates



locations = open_locations()
create_location("forest", "endless trees", locations)
create_location("swamp", "endless swamp", locations)
links = open_links()
create_link("forest", "swamp", "north", links)
validate_check_duplicates(locations)
validate_links(links, locations)
demjson.encode_to_file("locations.json",locations, overwrite=True)
demjson.encode_to_file("links.json", links, overwrite=True)

