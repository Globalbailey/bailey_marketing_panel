
from gmcapp.models import ChromeUserData

Chrome_user = ChromeUserData.objects.first()

chrome_user_path = Chrome_user.chrome_user_path

user_dir = 'user-data-dir='

Chrome_path = r"{}{}".format(user_dir, chrome_user_path)
