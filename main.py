from instagrapi import Client
from secrets import USERNAME, PASSWORD
from time import sleep



cl = Client()
cl.login(USERNAME, PASSWORD)



def follow_and_like_users_by_tag(tag: str, amount: int = 10):
    medias = cl.hashtag_medias_recent(tag, amount)
    for media in medias:
        id = media.dict()['user']['pk']
        media_pk = media.dict()['pk']
        user_followers = cl.user_following(cl.user_id)
        if id not in user_followers:
            try:
                cl.user_follow(id)
                print(f'Followed {id}')     
            except:
                print(f'Failed to follow {id}')
        try:
            cl.media_like(media_pk)
            print(f'Liked {media_pk}')
        except:
            print(f'Failed to like {media_pk}')
        
    return {'message': 'Followed and Liked users by tag'}

def follow_users_by_tag(tag: str, amount: int = 10):
    medias = cl.hashtag_medias_recent(tag, amount)
    for media in medias:
        id = media.dict()['user']['pk']
        user_followers = cl.user_following(cl.user_id)
        if id not in user_followers:
            try:
                cl.user_follow(id)
                print(f'Followed {id}')
            except:
                print(f'Failed to follow {id}')
    return {'message': 'Followed users by tag'}
        

def like_users_by_tag(tag: str, amount: int = 10):
    medias = cl.hashtag_medias_recent(tag, amount)
    for media in medias:
        media_pk = media.dict()['pk']
        try:
            cl.media_like(media_pk)
            print(f'Liked {media_pk}')
        except:
            print(f'Failed to like {media_pk}')
    return {'message': 'Liked users by tag'}

def unfollow_users_who_is_not_following():
    followers = cl.user_followers(cl.user_id)
    following = cl.user_following(cl.user_id)
    not_following_back = [user for user in following if user not in followers]
    print(not_following_back)
    for users in not_following_back:
        cl.user_unfollow(users)
        print(f'Unfollowed {users}')
        sleep(5)
    
            

    
#follow_and_like_users_by_tag('followforfollow', 2)

unfollow_users_who_is_not_following()
