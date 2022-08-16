from pathlib import Path

class FileHandler:
    def checkFileExists(self, file):
        p = Path(file)

        return p.exists()

    def readFile(self, file):
        if self.checkFileExists(file):
            whFile = open(file, "r")

            return whFile.read()

        return None

    def writeFile(self, file, data):
        if self.checkFileExists(file):
            whFile = open(file, "w")

            whFile.write(data)

            return True

        return False