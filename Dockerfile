FROM Ububtu:14.04

RUN apt install pyhton3 -y

Run pip install -r requirments.txt -y

Copy flask-API-app.py /root/flask

CMD ["pyhton3" "flask-API-app.py"]
