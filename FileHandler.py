from pathlib import Path

class FileHandler:
    def checkPathExists(self, file):
        p = Path(file)

        return p.exists()

    def checkFileExists(self, file):
        p = Path(file)

        return p.is_file()

    def readFile(self, file):
        if self.checkPathExists(file):
            whFile = open(file, "r")

            return whFile.read()

        return None

    def writeFile(self, file, data):
        if self.checkPathExists(file):
            whFile = open(file, "w")

            whFile.write(data)

            return True

        return False