import boto3

dynamodb_resource = boto3.resource('dynamodb', region_name='us-east-1')  # Specify your region
table = dynamodb_resource.Table('pokemon')  # Replace with your table name


def addPokemon(pokemon):
    print(pokemon)
    # Data to be inserted
    item = pokemon
    # Insert the item into the table
    table.put_item(Item=item)
    
    

def fetchFromDb():
        # Scan the table with a filter
        response = table.scan()

        items = response.get('Items', [])
        return items
        # for item in items:
        #     if item['name'] == pokemon:
        #          print(item)
        #     else: print("nah")    
            
            