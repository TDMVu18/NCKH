import pandas as pd
import function

start_url = 'https://www.facebook.com'
# Login
function.login(start_url)

# Crawl
# urls = ["https://www.facebook.com/thang0962472324",
#         "https://www.facebook.com/jijivishaphuoc",
#         "https://www.facebook.com/Sperm.Detective",
#         "https://www.facebook.com/Tuilathanhhungday",
#         "https://www.facebook.com/stc1702"
#         ]

urls = ['https://www.facebook.com/profile.php?id=100093434710364', 
        'https://www.facebook.com/profile.php?id=100093417395348', 
        'https://www.facebook.com/profile.php?id=100092725732662', 
        'https://www.facebook.com/profile.php?id=100092291003966']

for url in urls:
    name = function.get_name(url)
    total_friend = function.get_total_friend(url)
    place = function.get_about_place(url)
    gender = function.get_gender(url)
    date_of_birth = function.get_date_of_birth(url)[0]
    year = function.get_date_of_birth(url)[1]
    print(name, total_friend, place, gender, date_of_birth, year)

# data = [
#     {'name': name, 'place': place, 'gender': gender, 'date_of_birth': date_of_birth, 'year': year}
# ]
# # columns = ('name', 'place', 'gender', 'date_of_birth', 'year')

# df = pd.DataFrame(data)
# print(df)