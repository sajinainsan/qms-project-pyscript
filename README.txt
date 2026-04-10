Before running this program. Make sure to create a folder named 'database' at the same directory as the program's file.
The file directory should look like this:

 📂 project_folder/
  ├── 📂 database/
  │    ├── 📄 QD20260404.txt
  │    └── 📄 ...
  ├── 🖥️ que_sys.py
  └── 📄 README.txt



👨🏻‍💻 Devs log:

Before we created the program, we've first planned the console inteface and we're not surprised that some of it were edited and removed for optimization purposes.

💾 Final Output

 🖥️ ===========================
  │  REGISTRAR QUEUEING SYSTEM
  │ ===========================
  │ Search/Create New File.
  │ Order: QD[yyyymmdd]
  │ Filename: QD________
  │
  └── 🗃️ ==========================
       │          QDYYYYMMDD
       │  ==========================
       │  [1] - Review Queue
       │  [2] - View/Manage List 
       │  [3] - Register
       │  [ ] - Close
       │  What do you want: ___
       │
       ├── 📊 ===========================
       │              QUEUE STATS
       │       ===========================
       │       Total:                 ××××
       │       On-going:              ××××
       │       Done:                  ××××
       │       Missed:                ××××
       │
       ├── 💠 ======================================
       │       Num. | ID      | Name                  
       │       ======================================
       │       0001 | ××××××× | ------------------... 
       │       0002 | ××××××× | ------------------...
       │       0003 | ××××××× | ------------------...
       │       0004 | ××××××× | ------------------...
       │       0005 | ××××××× | ------------------... 
       │       ======================================
       │       [1] Next     [2] Skip     [ ] Close
       │       What do you want: ___
       │
       └── 📝 ==========================
                       REGISTER
               ==========================
               7-Character ID: _______
               Enter Name: ___________
               Registration Complete.


📄 New '.txt' File Format

 Status   | Num. | ID      | Name    
 -------- | ×××× | ××××××× | -----------------...


📄 Old '.txt' File Format

 ==========================
 Status: --------
 Number: ××××
 ID: ×××××××
 Name: -----------------...
 ==========================


📅 Marked Dates:

02-25-2026: Project Assignment 
02-26-2026: Brainstorming Ideas
03-04-2026: Project Proposal Compilation
03-04-2026: Program Demo Testing 
03-06-2026: Project Proposal Submission
03-18-2026: Project Proposal Approval
03-19-2026: Adding more features
04-04-2026: Program Completion
04-10-2026: Bug Fix: Resolved data corruption caused by input interruption
