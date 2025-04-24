var vbs = WDS.vars.get("vbsPath");
var file1 = WDS.vars.get("filepath1");
var file2 = WDS.vars.get("filepath2");

// Add quotes to file paths
var quotedFile1 = '"' + file1 + '"';
var quotedFile2 = '"' + file2 + '"';

// Build the command
var command = 'wscript "' + vbs + '" ' + quotedFile1 + ' ' + quotedFile2;
WDS.log.info("Executing: " + command);

// Execute
var proc = java.lang.Runtime.getRuntime().exec(command);
var exitCode = proc.waitFor();