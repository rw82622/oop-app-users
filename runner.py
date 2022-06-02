from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

free_user = FreeUser("Rex", "rex@gmail.com", "H384")
free_user.create_post("posting 1")
free_user.create_post("posting 2")
free_user.create_post("posting 3")

print(free_user.posts == ['posting 1', 'posting 2'])