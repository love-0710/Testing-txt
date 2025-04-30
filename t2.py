import java.nio.file.*
import java.io.*

def raw = prev.getResponseDataAsString()

if (!raw || !raw.contains("email_subjct")) {
    log.error("Response is empty or 'email_subjct' column not found.")
    return
}

def lines = raw.split('\n')

// Find column index
def headers = lines[0].split('\t')
def colIndex = headers.findIndexOf { it.trim().equalsIgnoreCase("email_subjct") }

if (colIndex == -1) {
    log.error("'email_subjct' column not found in headers.")
    return
}

// Write to CSV
def file = new File("email_subjects.csv")
def writer = new BufferedWriter(new FileWriter(file))
writer.write("email_subjct\n")

lines.drop(1).each { line ->
    def cols = line.split('\t')
    if (cols.size() > colIndex) {
        writer.write((cols[colIndex] ?: "") + "\n")
    }
}

writer.close()
log.info("Saved 'email_subjct' column to email_subjects.csv")