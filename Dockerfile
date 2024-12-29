FROM python:3.9-slim

# directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=flask_LR_API.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]







# docker build -t flask_lr_api .

# docker run -p 5000:5000 flask_lr_api

