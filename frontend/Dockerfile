# This file is used to build the docker image for the frontend
FROM python:3.9

#Set the working directory
WORKDIR /home

#Install the requirements
COPY requirements.txt .

RUN pip3 install --upgrade pip

#Install the requirements
RUN pip install -r requirements.txt

#Expose port
EXPOSE 8080

#Copy the app.py file
COPY . .

#Start the streamlit app
CMD ["streamlit", "run","app.py"]