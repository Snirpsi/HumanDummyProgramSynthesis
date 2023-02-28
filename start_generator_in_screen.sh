screen -dmS "ProgramGenerator" 

screen -S "ProgramGenerator" -p 0 -X stuff "python3 generatePrograms.py\n"