# base image (the onbuild version automatically copies your files and dependencies)
FROM python:3-onbuild


# specify the port number where we want our app to 
# be exposed
EXPOSE 8000

# innstall some dependencies for our app
RUN apt-get update  
# RUN pip install -r requirements.txt

CMD = ["python", "manage.py", "runserver"]
