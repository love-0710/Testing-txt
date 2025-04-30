import java.io.FileWriter
import java.io.BufferedWriter
import java.io.File

// Output CSV file path
def outputFile = new File("email_subjects.csv") // Change to full path if needed

// Create writer
def writer = new BufferedWriter(new FileWriter(outputFile))

// Get ResultSet from JDBC request
def rs = vars.getObject("ResultSet")
def meta = rs.getMetaData()
int colCount = meta.getColumnCount()

// Find the column index for 'email_subjct'
int targetIndex = -1
for (int i = 1; i <= colCount; i++) {
    if (meta.getColumnLabel(i).equalsIgnoreCase("email_subjct")) {
        targetIndex = i
        break
    }
}

if (targetIndex == -1) {
    log.error("Column 'email_subjct' not found.")
    writer.write("ERROR: Column 'email_subjct' not found.\n")
} else {
    writer.write("email_subjct\n") // CSV header
    while (rs.next()) {
        def value = rs.getString(targetIndex)
        writer.write(value?.replaceAll("[\\r\\n]+", " ") ?: "") // Clean line breaks
        writer.newLine()
    }
}

writer.close()
log.info("email_subjct column values saved to email_subjects.csv")