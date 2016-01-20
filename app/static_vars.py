JobType = {
  'B' : '<a class="ui green label">Backup Job</a>',
  'M' : '<a class="ui violet label">Migrated Job</a>',
  'V' : '<a class="ui yellow label">Verify Job</a>',
  'R' : '<a class="ui blue label">Restore Job</a>',
  'C' : '<a class="ui yellow label">Console program (not in database)</a>',
  'I' : '<a class="ui green label">Internal or system Job</a>',
  'D' : '<a class="ui red label">Admin Job</a>',
  'A' : '<a class="ui yellow label">Archive Job (not implemented)</a>',
  'C' : '<a class="ui yellow label">Copy Job</a>',
  'M' : '<a class="ui yellow label">Migration Job</a>',
}

JobStatus = {
  'C' : '<a class="ui brown label">Created but not yet running</a>',
  'R' : '<a class="ui teal label">Running</a>',
  'B' : '<a class="ui pink label">Blocked</a>',
  'T' : '<a class="ui green label">Terminated normally</a>',
  'W' : '<a class="ui olive label">Terminated normally with warnings</a>',
  'E' : '<a class="ui orange label">Terminated in Error</a>',
  'e' : '<a class="ui yellow label">Non-fatal error</a>',
  'f' : '<a class="ui red label">Fatal error</a>',
  'D' : '<a class="ui purple label">Verify Differences</a>',
  'A' : '<a class="ui grey label">Canceled by the user</a>',
  'I' : '<a class="ui grey label">Incomplete Job</a>',
  'F' : '<a class="ui blue label">Waiting on the File daemon</a>',
  'S' : '<a class="ui blue label">Waiting on the Storage daemon</a>',
  'm' : '<a class="ui blue label">Waiting for a new Volume to be mounted</a>',
  'M' : '<a class="ui blue label">Waiting for a Mount</a>',
  's' : '<a class="ui blue label">Waiting for Storage resource</a>',
  'j' : '<a class="ui blue label">Waiting for Job resource</a>',
  'c' : '<a class="ui blue label">Waiting for Client resource</a>',
  'd' : '<a class="ui blue label">Wating for Maximum jobs</a>',
  't' : '<a class="ui blue label">Waiting for Start Time</a>',
  'p' : '<a class="ui blue label">Waiting for higher priority job to finish</a>',
  'i' : '<a class="ui grey label">Doing batch insert file records</a>',
  'a' : '<a class="ui yellow label">SD despooling attributes</a>',
  'l' : '<a class="ui yellow label">Doing data despooling</a>',
  'L' : '<a class="ui yellow label">Committing data (last despool)</a>',
}
