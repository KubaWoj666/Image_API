# Image_API
Image API built in Django Rest Framework

# First version of the project **(branch: master):**
- simpler version of the project
- The database consists of two models. There are two views available: List and Detail.

# Second version of the project **(branch: main):**
- The database consists of five models: CustomUser, AccountTiers, Images, ThumbnailsSize, and Thumbnail.
- After the first migration new signal is triggered that automatically creates three AccountTiers (Basic, Premium, and Enterprise).
- The admin has the ability to create their own AccountTier.
- After creating a new Image by a user, a signal is sent which creates a Thumbnail based on the ThumbnailSizes obtained from AccountTiers.

# Set UP
- git clone -b main https://github.com/KubaWoj666/Image_API.git
- pip install -r requirements.txt
- python manage.py makemigrations core
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

