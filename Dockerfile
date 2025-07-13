FROM Ububtu:latest

RUN apt install pyhton3 -y

Run pip install -r requirments.txt 

Copy flask-API-app.py /root/flask

CMD ["pyhton3" "flask-API-app.py"]
