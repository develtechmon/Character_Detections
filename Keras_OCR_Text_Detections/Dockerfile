FROM python:3.8

# copy all the files to the container
WORKDIR /usr/src/app

COPY . .

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# tell the port number the container should expose
EXPOSE 80

# run the command

