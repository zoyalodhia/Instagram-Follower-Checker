# add the users you want to the respective files

unfollow_file = 'unfollow_accounts.txt'

# open, read and close file (those who follow you)
followers_list = open("followers.txt", "r")
followers = followers_list.readlines()
followers_list.close()

# open, read and close file (those who you follow)
following_list = open("following.txt", "r")
following = following_list.readlines()
following_list.close()

print ("\nUNFOLLOW THESE ACCOUNTS:\n")

# checks that every user in the following file is in the followers file, if not it will print the user add them to the unfollow file
unfollow = open(unfollow_file, 'w')
for i in following:
  if i not in followers:
    print (i) 
    unfollow.write(i)

# close unfollow file
unfollow.close()
