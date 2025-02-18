import os
import sqlalchemy as sa

CONNECTION_STRING = 'crate://localhost:4200'



# Connect to CrateDB using SQLAlchemy.
engine = sa.create_engine(
    CONNECTION_STRING, 
    echo=sa.util.asbool(os.environ.get("DEBUG", "false")))
connection = engine.connect()

# Community Areas

_ = connection.execute(sa.text(
"""
CREATE TABLE IF NOT EXISTS community_areas (
   areanumber INTEGER PRIMARY KEY,
   name TEXT,
   details OBJECT(DYNAMIC) AS (
       description TEXT INDEX USING fulltext,
       population BIGINT
   ),
   boundaries GEO_SHAPE INDEX USING geohash WITH (PRECISION='1m', DISTANCE_ERROR_PCT=0.025)
);
"""))

# Taxis

_ = connection.execute(sa.text(
"""
CREATE TABLE IF NOT EXISTS taxis (
   vehicleid INTEGER,
   status TEXT,
   make TEXT,
   model TEXT,
   modelyear INTEGER,
   color TEXT,
   fuel TEXT,
   wheelchairaccessible BOOLEAN,
   operator TEXT,
   zipcode TEXT,
   affiliation TEXT,
   medallion TEXT
);"""))

# Taxi Rides

_ = connection.execute(sa.text("""
CREATE TABLE IF NOT EXISTS taxi_rides (
   tripid TEXT,
   vehicleid INTEGER,
   starttime TIMESTAMP,
   endtime TIMESTAMP,
   duration INTEGER,
   miles DOUBLE PRECISION,
   pickupcommunityarea SMALLINT,
   dropoffcommunityarea SMALLINT,
   fare DOUBLE PRECISION,
   tips DOUBLE PRECISION,
   tolls DOUBLE PRECISION,
   extras DOUBLE PRECISION,
   totalcost DOUBLE PRECISION,
   paymenttype TEXT,
   company TEXT,
   pickupcentroidlatitude DOUBLE PRECISION,
   pickupcentroidlongitude DOUBLE PRECISION,
   pickupcentroidlocation GEO_POINT,
   dropoffcentroidlatitude DOUBLE PRECISION,
   dropoffcentroidlongitude DOUBLE PRECISION,
   dropoffcentroidlocation GEO_POINT
);"""))

# 311 Calls

_  = connection.execute(sa.text(
"""
CREATE TABLE IF NOT EXISTS three_eleven_calls (
   srnumber TEXT,
   srtype TEXT,
   srshortcode TEXT,
   createddept TEXT,
   ownerdept TEXT,
   status TEXT,
   origin TEXT,
   createddate TIMESTAMP,
   lastmodifieddate TIMESTAMP,
   closeddate TIMESTAMP,
   week GENERATED ALWAYS AS date_trunc('week', createddate),
   isduplicate BOOLEAN,
   createdhour SMALLINT,
   createddayofweek SMALLINT,
   createdmonth SMALLINT,
   locationdetails OBJECT(DYNAMIC) AS (
       streetaddress TEXT,
       city TEXT,
       state TEXT,
       zipcode TEXT,
       streetnumber TEXT,
       streetdirection TEXT,
       streetname TEXT,
       streettype TEXT,
       communityarea SMALLINT,
       ward SMALLINT,
       policesector SMALLINT,
       policedistrict SMALLINT,
       policebeat SMALLINT,
       precinct SMALLINT,
       latitude DOUBLE PRECISION,
       longitude DOUBLE PRECISION,
       location GEO_POINT
   )
) PARTITIONED BY (week);
"""))

