from fastapi import FastAPI,Path,Query

mydb =[]
app=FastAPI()
@app.get('/items/{item_id}')
async def read_item(
    item_id:int=Path(...,title="the id of the item",ge=1,le=1000),
    q:str|None=Query(None,min_length=3,max_length=50)
):
    return {"ideam_id",item_id,}
@app.post("/items/data/")
async def mydata(newdata:int=Path(...,title="newdate upload",ge=3,le=1000),
            q:str|None=Query(None,min_length=3,max_length=50)     ):
        me= mydb.append(newdata)
        return{"new data add your data":mydata}