# System Requirements 
# python 2.7 +
# django 1.3.1

# Obtain a git hub account. (free)
https://github.com/

# Generate rsa keys:  # This allows you to get, view, edit files.
https://help.github.com/articles/connecting-to-github-with-ssh/

# Contact Kyle Parker to become a "Contributor"

# Checkout a version of the repo
# https://github.com/kpparker165/shfc
git clone https://github.com/kpparker165/shfc.git

# Make sure you have django installed on your computer. 
# You may need to install PIP onto your linux maching.
# Download the following file then execute it. (be in a location you want the file to be placed /home/<user_name>)
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py


# Install django 1.3.1
# Documentation located at https://django-document-tchinese.readthedocs.io/en/stable-1.3.x/intro/tutorial01.html
pip install django~=1.3.1

# move into the subfolder shfc and run
python manage.py runserver 127.0.0.1:8080

# You should now be able to go to your web browser and enter in the IP Address from above.




https://jeffknupp.com/blog/2012/02/09/starting-a-django-project-the-right-way/


