"""
Purpose: 
Creates a provenance log in rtf format at the path provided, inserting a varying date string for batch upload of publication folders to aptrust. 
Input: 
PubFolderVTCSApath: Path where provenance log needs to be created
InsString: String that needs to be inserted, changes with the date/time of ingestion
Output: ProvenanceLog.rtf created at the path provided
"""
from datetime import datetime
filename=PubFolderVTCSApath+"/ProvenanceLog.rtf"
  # Get today's date
today = datetime.today()
  # Format the date as YYYY MM DD
formatted_date = today.strftime("%Y%m%d")
f = open(filename,'w',encoding="utf-8")
f.write("{\\rtf1\\ansi {\\b Date\\tab Curator\\tab Action} "+"\\line\n"+
        "[InsertDate]\\tab [Insert Curator]\\tab [Insert Action]"+"\\line\n"+
        "[InsertDate]\\tab [Insert Curator]\\tab [Insert Action]"+"\\line\n"+
        "[InsertDate]\\tab [Insert Curator]\\tab [Insert Action]"+"\\line\n"+
        "[InsertDate]\\tab [Insert Curator]\\tab [Insert Action]"+"\\line\n"+
        "[InsertDate]\\tab [Insert Curator]\\tab [Insert Action]"+"\\line\n"+
        "[InsertDate]\\tab [Insert Curator]\\tab [Insert Action]"+"\\line\n"+
        "[InsertDate]\\tab [Insert Curator]\\tab [Insert Action]"+"\\line\n"+
        "}")
f.close()

