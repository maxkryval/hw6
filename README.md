### STEPS TO RUN APPLICATION

Navigate to your python projects directory and clone the repository/unpack .zip archive submitted through CMS.
```
git clone https://github.com/maxkryval/hw5.git
cd hw5
```
Install dependencies (requirements.txt)
```
pip install requirements.txt
```
Run bash command to start servers.
```
chmod +x start.sh
./start.sh
```
Insert sample data into DB.
```
curl -X POST http://localhost:8001/save \
     -H "Content-Type: application/json" \
     -d '{"key": "value"}'
```
Send request
```
curl -X POST http://localhost:8000/run-pipeline \
     -H "Authorization: Bearer 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"
```

### Authentication & Request Flow

The Client Service uses token-based authentication by validating the `Authorization` header against the `OPENROUTER_API_KEY` stored in the `.env` file. This ensures that only users with the correct token can trigger the processing pipeline.

### Request Flow

1. **Client** sends a POST request to `/run-pipeline` on the **Client Service**, including the token.
2. The **Client Service** fetches the latest record from the **Database Service**.
3. It forwards that data to the **Business Logic Service**, which calls the OpenRouter LLM.
4. The processed response is then saved back into the **Database Service**.
5. The final result is returned to the **Client**.


### EXAMPLE LOCAL USAGE (after servers started through bash command)
```
maxymkryval@Maxyms-Laptop practice5 % curl -X POST http://localhost:8001/save \
     -H "Content-Type: application/json" \
     -d '{"key": "value"}'
{"status":"saved","data":{"key":"value"}}%                                                                                                                                      
maxymkryval@Maxyms-Laptop practice5 % curl -X POST http://localhost:8000/run-pipeline \
     -H "Authorization: Bearer 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"
{"result":{"status":"saved","data":{"question":"What are LeBron James career points? Return just the number.","llm_response":"35,367"}}}%                                       
maxymkryval@Maxyms-Laptop practice5 % curl -X POST http://localhost:8000/run-pipeline \
     -H "Authorization: Bearer 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"

{"result":{"status":"saved","data":{"question":"What are LeBron James career points? Return just the number.","llm_response":"36,002"}}}%
```
