#Dictionary Sorting
numbers_dict = {
    10: 1,
    12: 2,
    23: 3,
    34: 4,
    5: 3
}
print("Dictionary Sorting")
print(sorted(numbers_dict))
print()

#Dictionary of dictionary of dictionary with social media followers of followers structure

social_media = {
    "you": {
        "friend1": {
            "friend_of_friend1_1": {
                "follower_count": 4,
                "followers": ["you", "friend2", "friend3", "friend4"],
                "following_count": 2,
                "following": ["you", "friend2"]
            },
            "friend_of_friend1_2": {
                "follower_count": 0,
                "following_count": 0
            }
        },
        "friend2": {
            "friend_of_friend2_1": {
                "follower_count": 0,
                "following_count": 0
            }
        }
    }
}

print("Dictionary social_media dictionary structure")
print(social_media)
print()
