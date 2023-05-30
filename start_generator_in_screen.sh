session_name="test"
screen -dmS $session_name 
screen -S $session_name -p 0 -X stuff "./activate.sh\n"
screen -S $session_name -p 0 -X stuff "python3 generate2_with_compile.py  2>&1 | tee output.log \n"
