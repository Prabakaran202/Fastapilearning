import fastapi from FastAPI


App=FastAPI()

@app.get('/')
async root():
   return {'message':'vanakkam da mappula '}

