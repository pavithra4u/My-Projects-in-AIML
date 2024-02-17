import json

# Read the JSON file
with open('/home/pavithra/Telugu_Interspeech_Task1_Train_labelled_12-08-2021_13-09/data.json', 'r') as file:
        data_list = json.load(file)

        # Check if the list is not empty
        if data_list:
                # Extract the desired fields from all elements
                    for element in data_list:
                               audioFilename = element.get('audioFilename', 'N/A')
                               with open('uttrfin.txt', 'a') as file:
                               # Print or use the extracted fields
                                    print(f"{audioFilename}, {audioFilename}", file=file)
        else:
                    print("JSON list is empty.")