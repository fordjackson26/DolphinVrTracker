# Mario Kart Wii Vr Tracker for Dolphin
## System Requirements
- you must have python3 installed
##### Necessary Packages
- struct
- sys
- os
- time
- seaborn
- pandas 
#### if you do not a package installed you can install it using the command:
- pip install (*package name*)
## Running the program
**You will need 2 things**
1. the path to your game save (***rksys.dat*** file)
   - Commonly at "C:\Users\(*username*)\Documents\Dolphin Emulator\Wii\title\00010004\524d4345\data\rksys.dat"
2. the licence you want to track
   - 1 - top left
   - 2 - top right
   - 3 - bottom left
   - 4 - bottom right

#### Navigate into the directory where you cloned the repo
**Run the command**
python3 Tracker.py (path to rksys.dat) licenceNumber
- ex: python3 Tracker.py F:\riivolution\save\RMCE\rksys.dat 2
  - *this would be for the top right licence*

##### During Runtime
-tracks vr
-Once no changes have been detected for a while
 - Graph of vr gains and losses displayed
 - Graph of average gain or loss on each track displayed