FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh
EXPOSE 8000

CMD ["./start.sh"]
