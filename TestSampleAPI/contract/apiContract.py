getApi={
   "definitions": {},
   "$schema": "http://json-schema.org/draft-07/schema#",
   "$id": "http://example.com/root.json",
   "type": "object",
   "properties": {
     "CategoryId": {
       "$id": "#/properties/CategoryId",
       "type": "integer"
     },
     "Name": {
       "$id": "#/properties/Name",
       "type": "string",
       "pattern": "^(.*)$"
     },
     "Path": {
       "$id": "#/properties/Path",
       "type": "string",
       "pattern": "^(.*)$"
     },
     "CanListAuctions": {
       "$id": "#/properties/CanListAuctions",
       "type": "boolean"
     },
     "CanListClassifieds": {
       "$id": "#/properties/CanListClassifieds",
       "type": "boolean"
     },
     "CanRelist": {
       "$id": "#/properties/CanRelist",
       "type": "boolean"
     },
     "LegalNotice": {
       "$id": "#/properties/LegalNotice",
       "type": "string"
     },
     "DefaultDuration": {
       "$id": "#/properties/DefaultDuration",
       "type": "integer"
     },
     "AllowedDurations": {
       "$id": "#/properties/AllowedDurations",
       "type": "array",
       "items": {
         "$id": "#/properties/AllowedDurations/items",
         "type": "integer"
       }
     },
     "Fees": {
       "$id": "#/properties/Fees",
       "type": "object",
       "properties": {
         "Bundle": {
           "$id": "#/properties/Fees/properties/Bundle",
           "type": "number"
         },
         "EndDate": {
           "$id": "#/properties/Fees/properties/EndDate",
           "type": "number"
         },
         "Feature": {
           "$id": "#/properties/Fees/properties/Feature",
           "type": "number"
         },
         "Gallery": {
           "$id": "#/properties/Fees/properties/Gallery",
           "type": "number"
         },
         "Listing": {
           "$id": "#/properties/Fees/properties/Listing",
           "type": "number"
         },
         "Reserve": {
           "$id": "#/properties/Fees/properties/Reserve",
           "type": "number"
         },
         "Subtitle": {
           "$id": "#/properties/Fees/properties/Subtitle",
           "type": "number"
         },
         "TenDays": {
           "$id": "#/properties/Fees/properties/TenDays",
           "type": "number"
         },
         "ListingFeeTiers": {
           "$id": "#/properties/Fees/properties/ListingFeeTiers",
           "type": "array",
           "items": {
             "$id": "#/properties/Fees/properties/ListingFeeTiers/items",
             "type": "object",
             "properties": {
               "MinimumTierPrice": {
                 "$id": "#/properties/Fees/properties/ListingFeeTiers/items/properties/MinimumTierPrice",
                 "type": "integer"
               },
               "FixedFee": {
                 "$id": "#/properties/Fees/properties/ListingFeeTiers/items/properties/FixedFee",
                 "type": "number"
               }
             }
           }
         },
         "SecondCategory": {
           "$id": "#/properties/Fees/properties/SecondCategory",
           "type": "number"
         }
       }
     },
     "FreePhotoCount": {
       "$id": "#/properties/FreePhotoCount",
       "type": "integer"
     },
     "MaximumPhotoCount": {
       "$id": "#/properties/MaximumPhotoCount",
       "type": "integer"
     },
     "IsFreeToRelist": {
       "$id": "#/properties/IsFreeToRelist",
       "type": "boolean"
     },
     "Promotions": {
       "$id": "#/properties/Promotions",
       "type": "array",
       "items": {
         "$id": "#/properties/Promotions/items",
         "type": "object",
         "properties": {
           "Id": {
             "$id": "#/properties/Promotions/items/properties/Id",
             "type": "integer"
           },
           "Name": {
             "$id": "#/properties/Promotions/items/properties/Name",
             "type": "string",
             "pattern": "^(.*)$"
           },
           "Description": {
             "$id": "#/properties/Promotions/items/properties/Description",
             "type": "string",
           },
           "Price": {
             "$id": "#/properties/Promotions/items/properties/Price",
             "type": "number"
           },
           "MinimumPhotoCount": {
             "$id": "#/properties/Promotions/items/properties/MinimumPhotoCount",
             "type": "integer"
           }
         }
       }
     },
     "EmbeddedContentOptions": {
       "$id": "#/properties/EmbeddedContentOptions",
       "type": "array"
     },
     "MaximumTitleLength": {
       "$id": "#/properties/MaximumTitleLength",
       "type": "integer"
     },
     "AreaOfBusiness": {
       "$id": "#/properties/AreaOfBusiness",
       "type": "integer"
     },
     "DefaultRelistDuration": {
       "$id": "#/properties/DefaultRelistDuration",
       "type": "integer"
     }
   }
 }