import boto3
import uuid
from A import A


class Database:
    counter = 0

    aws_access_key_id = ""
    aws_secret_access_key = ""
    aws_region = ""  
    dynamo = None
    table = None

    table_names = ["achievements", "games", "statistics", "store", "users"]

    table_inserts = None


    def __init__(self, **kwargs):
        super(Database, self).__init__(**kwargs)
        # self.dynamo = boto3.client(
        #     'dynamodb',
        #     aws_access_key_id=self.aws_access_key_id,
        #     aws_secret_access_key=self.aws_secret_access_key,
        #     region_name=self.aws_region
        # )
        self.dynamo = None

        self.table_inserts = {
            "users": {
                'id': self.create_data(str(uuid.uuid4())),
                'avatar': self.create_data(""),
                'email': self.create_data(""),
                'friends': self.create_data(""),
                'realname': self.create_data(""),
                'last_login': self.create_data(""),
                'username': self.create_data("")
            },

            "games": {
                'id': self.create_data(""),
                'gamedate': self.create_data(""),
                'erasers_collected': self.create_data(""),
                'erasers_used': self.create_data(""),
                'shields_collected': self.create_data(""),
                'shields_used': self.create_data(""),
                'slows_collected': self.create_data(""),
                'slows_used': self.create_data(""),
                'stops_collected': self.create_data(""),
                'stops_used': self.create_data(""),
                'time_played': self.create_data(""),
                'letter_sets': self.create_data(""),
                'words_spelled': self.create_data(""),
                'points': self.create_data(""),
                'user_id': self.create_data(""),
                'game_number': self.create_data(""),
                'bomb_mines': self.create_data(""),
                'grow_mines': self.create_data(""),
                'freeze_mines': self.create_data(""),
                'blind_mines': self.create_data(""),
                'shrink_mines': self.create_data("")
            },

            "statistics": {
                'id': self.create_data(""),
                'erasers_collected': self.create_data(""),
                'erasers_used': self.create_data(""),
                'games_played': self.create_data(""),
                'games_won': self.create_data(""),
                'shields_collected': self.create_data(""),
                'shields_used': self.create_data(""),
                'slows_collected': self.create_data(""),
                'slows_used': self.create_data(""),
                'stops_collected': self.create_data(""),
                'stops_used': self.create_data(""),
                'time_played': self.create_data(""),
                'top_1': self.create_data(""),
                'top_3': self.create_data(""),
                'top_5': self.create_data(""),
                'top_10': self.create_data(""),
                'total_points': self.create_data(""),
                'words_spelled': self.create_data(""),
                'bomb_mines': self.create_data(""),
                'grow_mines': self.create_data(""),
                'freeze_mines': self.create_data(""),
                'blind_mines': self.create_data(""),
                'shrink_mines': self.create_data("")
            },

            "achievements": {
                "id": self.create_data(""),
                "10_letter_word": self.create_data(False),
                "2_languages": self.create_data(False),
                "3_languages": self.create_data(False),
                "4_languages": self.create_data(False),
                "5_languages": self.create_data(False),
                "7_letter_word": self.create_data(False),
                "8_letter_word": self.create_data(False),
                "9_letter_word": self.create_data(False),
                "blinded_word": self.create_data(False),
                "collect_100_gold": self.create_data(False),
                "collect_1000_gold": self.create_data(False),
                "collect_10000_gold": self.create_data(False),
                "collect_500_gold": self.create_data(False),
                "collect_5000_gold": self.create_data(False),
                "enlarged_word": self.create_data(False),
                "frozen_word": self.create_data(False),
                "less_than_10_minutes": self.create_data(False),
                "no_game_over": self.create_data(False),
                "no_powerups": self.create_data(False),
                "win_1_game": self.create_data(False),
                "win_10_games": self.create_data(False),
                "win_100_games": self.create_data(False),
                "win_25_games": self.create_data(False),
                "win_5_games": self.create_data(False),
                "win_50_games": self.create_data(False),
                "with_1_strike": self.create_data(False)
            },

            "inventory": {
                "id": self.create_data(""),
                "backgrounds": self.create_data(0),
                "coins": self.create_data(0),
                "music": self.create_data(0),
                "paid_version": self.create_data(False),
                "shield": self.create_data(0),
                "shrink": self.create_data(0),
                "skins": self.create_data(0),
                "slow": self.create_data(0),
                "stop": self.create_data(0),
                "strike": self.create_data(0)
            }

        }



    def set_table(self, name):
        self.table = name


    def create_data(self, data):
        try:
            try:
                data = data["BOOL"] 
                return {"BOOL": data}
            except:
                pass
        
            try:
                data = data["S"] 
                return {'S': str(data)}
            except:
                pass

            data = data
            
            return {'S': str(data)} if isinstance(data, bool) == False else {'BOOL': bool(data)} if isinstance(data, bool) == True else {'N': int(data)}
        except Exception as e:
            print("\n\nError in 'Database' class, 'create_data' function:\n\n", e, "\n\n")
            return ""
    

    def create_list(self, data):
        if A().root().login_required == True:
            new_list = []

            for item in data:
                new_list.append(self.create_data(item))

            return {
                "L": new_list
            }
        else: 
            new_list = data
    

    def get_data(self, data):
        if A().root().login_required == True:
            try:
                data = data["S"] 
                return str(data)
            except:
                pass

            try:
                data = data["BOOL"]
                return data
            except:
                pass     

            data = data   
            return str(data) if isinstance(data, bool) == False else bool(data) if isinstance(data, bool) == True else int(data)
        else:
            return data
    

    def add_data(self, value1, value2):
        if A().root().login_required == True:
            try:
                try:
                    value1 = value1["S"]
                except:
                    value1 = value1
            
                try:
                    value2 = value2["S"]
                except:
                    value2 = value2
                return {'S': str(int(value1) + int(value2))}
            except Exception as e:
                print("\n\nError in 'Database' class, 'add_data' function:\n\n", e, "\n\n")
                return 0
        else:
            return str(value1 + value2)
    

    def subtract_data(self, value1, value2):
        if A().root().login_required == True:
            try:
                value1 = value1["S"]
            except:
                value1 = value1
        
            try:
                value2 = value2["S"]
            except:
                value2 = value2

            return {'S': str(int(value1) - int(value2))}
        else:
            return str(int(value1) - int(value2))
    

    def set_insert(self, table, data):
        try:
            self.table_inserts[table] = data
        except:
            print("\n\nTable insert error in 'Database' class, 'set_insert' function. Setting to blank object.")
            self.table_inserts[table] = {}


    def insert(self, table, data):
        if A().root().login_required == True:
            try:
                response = self.dynamo.put_item(
                    TableName=table,
                    Item=data
                )
            except Exception as e:
                print("\n\nTable insert error in 'Database' class, 'insert' function. Item: \n\n" + str(data) + "\n\n not inserted.")
                print("PutItem failed:", e)
        else: 
            print("\n\nNo insert. Game is offline.")
         


    def retrieve(self, table, column, value, all=False):
        if A().root().login_required == True:
            try:
                response = self.dynamo.scan(
                    TableName=table,
                    FilterExpression=column + '= :val',
                    ExpressionAttributeValues={
                        ':val': value
                    }
                )

                if all:
                    return response.get('Items')    
                return response.get('Items')[0]
            except:
                print("\n\nretrieve fail")
        else:
            print("\n\nNo retrieve. Game is offline.")
            return {}
            

    def retrieve_all(self, table):
        if A().root().login_required == True:
            try:
                response = self.dynamo.scan(
                    TableName=table,
                )
        
                return response.get('Items')

            except:
                print("\n\nretrieve fail")
        else:
            print("\n\nNo retrieve all. Game is offline.")
            return {}      


    def find(self, table, column, value):
        if A().root().login_required == True:
            response = self.dynamo.scan(
                TableName= table,
                FilterExpression=column + ' = :val',
                ExpressionAttributeValues={
                    ':val': value
                }
            )

            return True if len(response.get('Items')) > 0 else False
        else:
            return False
    

    def update(self, table, id, data):
        if A().root().login_required == True:
            self.dynamo.update_item(
                TableName=table,
                Key={
                    'id': self.create_data(id) 
                },
                UpdateExpression=self.update_expression(data),
                ExpressionAttributeValues=self.update_values(data),
                ReturnValues="UPDATED_NEW"
            )

            A().main().user_data = A().main().database.retrieve("users", "username", A().main().database.create_data(A().main().username)) if table == "users" else A().main().user_data
        else:
            print("\n\nNo retrieve all. Game is offline.")


    def update_expression(self, data):
        if A().root().login_required == True:
            expr = "set "
            i = 1
            for column in list(data.keys()):
                expr = expr + column + " = :val" + str(i) 
                expr = expr + ", " if i < len(list(data.keys())) else expr
                i += 1
            return expr
        else:
            print("\n\nNo update expression. Game is offline.")
    

    def update_values(self, data):
        if A().root().login_required == True:
            values = {}
            i = 1
            for item in list(data.keys()):           
                item = self.get_data(item)
                values[":val" + str(i)] = data[item] 
                i += 1 
            return values
        else:
            print("\n\nNo update values. Game is offline.")


    def increment(self, table, column, id):
        if A().root().login_required == True:
            try:
                data = self.retrieve(table, column, id, True)
                greatest = 0
                for row in data:
                    if row:
                        greatest = int(self.get_data(row["game_number"])) if int(self.get_data(row["game_number"])) and int(self.get_data(row["game_number"])) > greatest else None
                if data:
                    return greatest
                else:
                    return int(0)
            except Exception as e:
                print("\n\nError in 'Database' class, 'increment' function:\n\n", e, "\n\n")
                return 0
        else:
            print("\n\nNo increment. Game is offline.")