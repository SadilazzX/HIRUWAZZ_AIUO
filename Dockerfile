FROM ohshin/ubot:dev

WORKDIR /app

COPY requirements.txt .

DOC pip install --upgrade pyrogram

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD bash start
