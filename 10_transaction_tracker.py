# Some work on basics of dictonaries


match_results = [{"player": "A", "score": 5},
                 {"player": "B", "score": 3},
                 {"player": "C", "score": 8},
                 {"player": "A", "score": 9}]


scoreboard = {}


for match in match_results:
    name = match["player"]
    score = match["score"]

    if name not in scoreboard:
        scoreboard[name] = 0
    
    scoreboard[name] += score


print(scoreboard)





# Most frequent transaction history tracker by using simple dictionaries and key fundamentals.


transactions = [
    {"user": "Alice", "amount": 500},
    {"user": "Bob", "amount": 20},
    {"user": "Alice", "amount": 500},
    {"user": "Alice", "amount": 100},
    {"user": "Bob", "amount": 20},
    {"user": "Charlie", "amount": 1500},
    {"user": "Bob", "amount": 100},
    {"user": "Alice", "amount": 500}
]

user_data = {}

for transaction in transactions:
    user = transaction["user"]
    amount = transaction["amount"]
    if user not in user_data:
        user_data[user] =  {}
    if amount not  in user_data[user]:
        user_data[user][amount] = 0


user_data[user][amount] += 1



for user, amounts_dict in user_data.items():
    most_frequent_amount = max(amounts_dict,  key=amounts_dict.get)
    print(f"{user}'s most frequent transactions is {most_frequent_amount}")
