தேவைகள் (Requirements):
Schemas (App/schemas/inventory.py):

Product மாடல்ல: id (int), name (str - min 3 chars), price (float - gt 0), stock (int - ge 0), category (str).

Routes (App/routes/inventory.py):

GET /inventory/: எல்லா பொருட்களையும் காட்டணும்.

GET /inventory/search: இதுல ரெண்டு Query Parameters இருக்கணும்: min_price மற்றும் max_price. இந்த விலைக்குள் இருக்கும் பொருட்களை மட்டும் ஃபில்டர் பண்ணி எடுக்கணும்.

GET /inventory/out-of-stock: எதெல்லாம் stock == 0-ன்னு இருக்கோ, அந்தப் பொருட்களை மட்டும் காட்டணும்.

POST /inventory/add: புதுப் பொருளைச் சேர்க்கணும்.

Main (App/main.py):

இந்த inventory ரூட்டரை மெயின் ஆப்ல include_router பண்ணனும்.



HTML input
   ↓
JavaScript value edukkum
   ↓
API call (fetch)
   ↓
Backend process pannum
   ↓
Response thirumba JS
   ↓
HTML-la display
