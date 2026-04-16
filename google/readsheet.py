from googleapiclient.errors import HttpError

def call(service, id, range):
    try:
        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=id, range=range)
            .execute()
        )

        rows = result.get("values", [])
        return rows
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def read(service):   
    with open('google\sheetinfo.txt', 'r') as info:
        lines = info.readlines()
        lines = [line.rstrip("\n") for line in lines]
        
        id = lines[1]
        name = lines[3]
        player_column = lines[5]
        rating_column = lines[7]
        rows = lines[9].split(':')
        
        start = rows[0]
        end = rows[1]

        sheet_range = f"\'{name}\'!{player_column}{start}:{rating_column}{end}"

        players = call(service, id, sheet_range)
        
        player_dict = {}
        for player in players:
            player_dict[player[0]] = player[2]
        
        return player_dict