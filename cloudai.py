#This Project is Just the begenning of Friendly AI in technical World 
#!/usr/bin/python3

import os
print("Welcome to World of Lilly ")
loc = input("\nDo you wish to run commands locally or remote?\n")

print("\n Oh!! Great! you choose me ")
while(True):
    print("""        Here are your options:
        ----------------------
        
        PRESS 0 TO EXIT
        COMMON COMMANDS
        ---------------
        S1. Date
        S2. Calender
        S3. NIC
        CONFIGURATIONS
        --------------
        C1. Configure yum
        C2. Configure Webserver
        C3. Configure Docker
        ADDITIONAL STORAGE /  DRIVES
        ----------------------------
        M1. Create Static Partition
        M2. Delete Static Partition
        M3. Format partition
        M4. Mount to folder
        M5. Unmount from folder
        M6. Create VG - LVM (Dynamic Partition)
        M7. Extend LVM size
        DOCKER
        ------
        D1. Run container
        D2. Stop container
        D3. Restart container and get shell access
        D4. Delete container
        D5. Show running containers
        D6. Show stopped containers
        
        HADOOP
        ------
        H1. Configure Client
        H2. Configure NameNode
        H3. Configure DataNode
        H4. Report
        H5. List Data
        H5. Put Data
        H6. Get Data
        H7. Remove Data
        """)
