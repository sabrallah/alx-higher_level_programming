#!/bin/bash
# Makes request 0.0.0.0:5000/catch_me and causes server respond "You got me!"
curl -sLX PUT -H "Origin: alxafrica" -d "user_id=98" 0.0.0.0:5000/catch_me
