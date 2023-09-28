#!/bin/bash
# Makes request 0.0.0.0:5000/catch_me and causes server respond "You got me!"
curl -sLX PUT -d "user_id=98" -H "Origin: AlxAfrica" 0.0.0.0:5000/catch_me
