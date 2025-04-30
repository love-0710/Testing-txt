import java.sql.ResultSet
import java.io.FileWriter
import java.io.BufferedWriter

// Get the result set object
def rs = prev.getResultSet()

if (rs == null) {
    log.error("ResultSet is NULL - check JDBC and JDBC Sampler connection.")
    return
}

def meta = rs.getMetaData()
int colCount = meta.getColumnCount()

// Find column index for 'email_subjct'
int targetIndex = -1
for (int i = 1; i <= colCount; i++) {
    if (meta.getColumnLabel(i).equalsIgnoreCase("email_subjct")) {
        targetIndex = i
        break
    }
}

// Prepare to write to CSV
def outputFile = new File("C:\\Users\\practice_project\\JMeter\\email_subjects.csv")
def writer = new BufferedWriter(new FileWriter(outputFile))

if (targetIndex == -1) {
    log.error("Column 'email_subjct' not found in ResultSet.")
    writer.write("email_subjct not found\n")
} else {
    writer.write("email_subjct\n")
    while (rs.next()) {
        def value = rs.getString(targetIndex)
        writer.write(value?.replaceAll("[\\r\\n]+", " ") ?: "")
        writer.newLine()
    }
}
writer.close()
log.info("Saved email_subjct values to CSV.")