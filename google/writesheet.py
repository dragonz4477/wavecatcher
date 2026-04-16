from googleapiclient.errors import HttpError

def call(service, id, cell):
    try:
        values = [
            ["boobs"]
        ]
        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .update(spreadsheetId=id, range=cell, valueInputOption="USER_ENTERED", body=body)
            .execute()
        )
        return
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
def write(service):
    call(service, "1gq-VNy7uqQbdfd0o_76XWYRByLjQvpOCn4Km-wi8nBc", "\'Rating Leaderboard\'!D5:D5")