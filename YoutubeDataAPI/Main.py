from googleapiclient.discovery import build

api_key = 'AIzaSyDElePC02zJxj4lzOjehNK7kOrqObK0NWc'

youtube = build('youtube',
                'v3',
                developerKey=api_key)

'''
request = youtube.channels().list(
    part='snippet , statistics',
    id='ApnaCollegeOfficial'
)
'''

request = youtube.videos().list(
    part='snippet , statistics',
    id='deztUdPApiM'
)

response = request.execute()

'''
if response['items']:
    print('Views:',response['items'][0]['statistics']['viewCount'])
    #response['items'][0]['statistics']['subscriberCount']
    #response['items'][0]['statistics']['videoCount']
else:
    print('Video not found')
'''

if response['items']:
    print('Title    :', response['items'][0]['snippet']['title'])
    print('Views    :', response['items'][0]['statistics']['viewCount'])
    print('Comments :', response['items'][0]['statistics']['commentCount'])
    print('Likes    :', response['items'][0]['statistics']['likeCount'])

    # print(f'Title: {title}')
    # print(f'Views: {views}')
    # print(f'Comments: {comments}')
    # print(f'Like: {like}')

else:
    print('Video not found')
