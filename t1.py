import java.io.File
import java.io.FileWriter
import java.io.BufferedWriter

// Output path (update as needed)
def outputFile = new File("C:\\Users\\practice_project\\JMeter\\email_subjects.csv")
def writer = new BufferedWriter(new FileWriter(outputFile))

// Get ResultSet object
def rs = vars.getObject("ResultSet")
if (rs == null) {
    log.error("ResultSet is null! Did JDBC request run correctly?")
    writer.write("ERROR: ResultSet is null.\n")
    writer.close()
    return
}

// Get metadata to find column index
def meta = rs.getMetaData()
int colCount = meta.getColumnCount()

// Locate column index of 'email_subjct'
int targetIndex = -1
for (int i = 1; i <= colCount; i++) {
    if (meta.getColumnLabel(i).equalsIgnoreCase("email_subjct")) {
        targetIndex = i
        break
    }
}

// Write to CSV
if (targetIndex == -1) {
    writer.write("ERROR: Column 'email_subjct' not found.\n")
} else {
    writer.write("email_subjct\n") // CSV header
    while (rs.next()) {
        def value = rs.getString(targetIndex)
        writer.write(value?.replaceAll("[\\r\\n]+", " ") ?: "")
        writer.newLine()
    }
}

writer.close()
log.info("Saved email_subjct values to email_subjects.csv")