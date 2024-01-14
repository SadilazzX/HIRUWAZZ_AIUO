FROM ohshin/ubot:dev

WORKDIR /app

COPY requirements.txt . 

RUN pip3 install --no-cache-dir --upgrade pyrogram -r requirements.txt

COPY . .

CMD bash start
