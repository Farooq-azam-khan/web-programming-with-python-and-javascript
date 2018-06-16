import requests

def main():
    res = requests.get("http://localhost:5000/api/flights/100")
    # print(res.text)
    data = res.json()    
    # print("data:",data)
    # print(data['destination'])
    if res.status_code == 200:
        print(f'A flight from {data["origin"]}, to {data["destination"]}, will take {data["duration"]}minutes')
        print(f'The passengers on that flight are {data["passengers"]}')
    else:
        print(data)

if __name__ == '__main__':
    main()