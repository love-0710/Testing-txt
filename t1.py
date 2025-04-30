import java.io.FileWriter
import java.io.BufferedWriter

def rs = vars.getObject("ResultSet")
if (rs == null) {
    log.error("ResultSet is null! Make sure 'Store as Object' is checked in JDBC Request.")
    return
}

def meta = rs.getMetaData()
int colCount = meta.getColumnCount()

// Find column index for email_subjct
int targetIndex = -1
for (int i = 1; i <= colCount; i++) {
    if (meta.getColumnLabel(i).equalsIgnoreCase("email_subjct")) {
        targetIndex = i
        break
    }
}

// Write to CSV
def file = new File("C:\\Users\\practice_project\\JMeter\\email_subjects.csv")
def writer = new BufferedWriter(new FileWriter(file))

if (targetIndex == -1) {
    writer.write("ERROR: email_subjct column not found\n")
} else {
    writer.write("email_subjct\n")
    while (rs.next()) {
        def value = rs.getString(targetIndex)
        writer.write(value?.replaceAll("[\\r\\n]+", " ") ?: "")
        writer.newLine()
    }
}

writer.close()
log.info("email_subjects.csv created successfully.")