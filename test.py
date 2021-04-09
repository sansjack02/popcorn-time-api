from media.tv import *
import dataclasses

#TV Class Object
tv = TV()

#this would be passed in from a react prop
imbd_id = "tt0773262"

# Gets Specific Show From Main Page
ret = [x for x in tv.GetPopular() if x["imbd_id"] == imbd_id ][0]

parsed = ret["torrent"] = tv.GetShow(ret["imbd_id"])

print(parsed)

#Search for specific film
print(tv.GetShow(imbd_id))


