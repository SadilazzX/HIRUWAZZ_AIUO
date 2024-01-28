FROM ohshin/ubot:dev

WORKDIR /app 

ls -ld /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "PyroUbot"]
