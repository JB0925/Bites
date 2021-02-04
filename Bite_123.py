from collections import defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships, users=users):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    all_friends = defaultdict(list)
    
    for friendship in friendships:
        person1, person2 = friendship
        all_friends[person1].append(users.get(person2))
        all_friends[person2].append(users.get(person1))
    
    most_friends = max(all_friends.items(), key=lambda x: len(x[1))
    return users.get(most_friends[0]), sorted(most_friends[1])





print(get_friend_with_most_friends(friendships))
