# Fast_API_example
Small FastAPI example working with terminal to understand the methods involved.

Script usings fastapi module aswell as introducing a pydantic model for handling complex data structures.
Course followed Youtube video: https://www.youtube.com/watch?v=iWS9ogMPOI0

# Main topics covered
## Post
Method to provide data to a server. Using a Curl post method as seen below, it stores the item.

curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=orange'

## Get
To return the list of items use the following method:
curl -X GET 'http://127.0.0.1:8000/items?limit=3'

This uses the list_item function and we specify a limit of 3 items to be returned to the list

## Error Handling
Error handling and status codes were implemented using the HTTPException library from FastAPI. Specifically for this example where if we return an out of index item, we present an easier to read message with an f string

## Pydantic Models
Tutorial briefly touched on Pydantic models and how more complex data structures can be passed into functions instead of simple strings. This included creating an Item class and providing it into some of the methods 