social_network = {
    'alice': ('Alice Smith', ['maria']),
    'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
    'joe': ('Joseph Adams', ['maria', 'eve']),
    'eve': ('Evelyn Cooper', ['joe']),
    'david': ('David Benson', ['maria'])
}
#part a
def add_user(sn, username, fullname):
    try:
        # Check if the user already exists
        if username in sn:
            raise ValueError('user already exists.')
        sn[username] = (fullname, [])
        print("user added successfully.")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False

#part b
def add_friend(sn, user1, user2):
    try:
        if user1 not in sn or user2 not in sn:
            raise ValueError("One or more users not found in the social network.")
        # Add user2 to user1's friends and vice versa
        sn[user1][1].append(user2)
        sn[user2][1].append(user1)
        print("They are now friends!")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False

#part c
def get_friends(sn, user1, distance):
    try:
        if user1 not in sn:
            raise ValueError("User not found in the social network.")

        result = set()  
        visited = set() 

        def pathway(user, current_distance):
            if current_distance > distance:
                return

            for friend in sn[user][1]:
                if friend not in visited and friend not in result:
                    visited.add(friend)
                    result.add(friend)
                    pathway(friend, current_distance + 1)

        pathway(user1, 1)
        result.discard(user1) #Chpt 9 "other set methods"
        return list(result)  # Convert set back to a list before returning
    except ValueError as e:
        print(f"Error: {e}")
        return []

import csv
#part d
def save_network(filename, sn):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(['Username', 'Full Name', 'Friends'])

            # Write data rows
            for username, (full_name, friends) in sn.items():
                writer.writerow([username, full_name] + friends)
        print(f"Social network saved to '{filename}' successfully.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")

#part e
def load_network(filename):
    try:
        sn = {}
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            # Skip header
            next(reader, None)
            for row in reader:
                username = row[0]
                full_name = row[1]
                friends = row[2:]
                sn[username] = (full_name, friends)
        return sn
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
#part d
# Adding a new user
print('part a')
add_user(social_network, 'john', 'John Doe')
add_user(social_network,'alice','Alice Smith')
print()

print('part b')
add_friend(social_network, 'alice', 'joe')
add_friend(social_network, 'alice', 'john')
print()

result_1 = get_friends(social_network, 'alice', 1)
result_2 = get_friends(social_network, 'alice', 2)
print ('part c: Friends of Alice at distance 1', result_1)
print ('Friends of Alice at distance 1', result_2)

print('part d')
save_network('social_network.csv', social_network)
print()
print('part e')
loaded_network = load_network('social_network.csv')
print("Loaded Social Network:", loaded_network)