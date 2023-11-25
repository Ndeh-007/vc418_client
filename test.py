import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMessageBox, \
    QLineEdit
from PySide6.QtCore import QProcess, Slot
import json
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QProcess Example")
        self.setGeometry(100, 100, 500, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.output_text_edit = QTextEdit()
        self.layout.addWidget(self.output_text_edit)

        self.process = QProcess()

        self.nprocsInput = QLineEdit()
        self.nprocsInput.setText("4")
        self.layout.addWidget(self.nprocsInput)

        self.loadJSONBtn = QPushButton("Load JSON")
        self.loadJSONBtn.clicked.connect(self.handle_load_json)
        self.layout.addWidget(self.loadJSONBtn)

        self.fetchJSONBtn = QPushButton("Fetch JSON")
        self.fetchJSONBtn.clicked.connect(self.handle_fetch_json)
        self.layout.addWidget(self.fetchJSONBtn)

        self.start_process_button = QPushButton("Start Server")
        self.start_process_button.clicked.connect(self.start_process)
        self.layout.addWidget(self.start_process_button)

    @Slot()
    def start_process(self):
        # Set the command to run here

        # Connect process signals
        self.process.readyReadStandardOutput.connect(self.read_output)
        self.process.readyReadStandardError.connect(self.read_error)
        self.process.errorOccurred.connect(self.handle_error)

        # self.process.setWorkingDirectory("C:\\Work\\School\\CPSC418\\Project\\vc418_server")
        self.process.setWorkingDirectory("E:\\Work\\School\\VCS418\\vc418_server")

        # Start the process
        self.process.start('C:\\Tools\\rebar3.cmd', ["shell", "--apps", "vc418_server"])

        if not self.process.waitForStarted():
            QMessageBox.critical(self, "Error", "Failed to start process.")
            return

        self.process.waitForFinished()

    @Slot()
    def handle_error(self, data):
        self.output_text_edit.append(str(data))

    @Slot()
    def read_output(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.output_text_edit.append(data)

    @Slot()
    def read_error(self):
        data = self.process.readAllStandardError().data().decode()
        self.output_text_edit.append(f"Error: {data}")

    def handle_fetch_json(self):
        nprocs = int(self.nprocsInput.text())

        url = f"http://localhost:8080/reduce?nprocs={nprocs}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                self.output_text_edit.append("fetch successful, writing to file \n")
                # write data to file
                with open("test.json", "w") as file:
                    data = response.json()
                    json.dump(data, file, indent=4)
                self.output_text_edit.append("write complete \n")
            else:
                self.output_text_edit.append(f"[Error] fetch failed with status code: {response.status_code}\n")
        except Exception as e:
            self.output_text_edit.append(str(e))

    def handle_load_json(self):
        # load the json data
        jsonData = self.load_json_file("test.json")
        # construct the binary tree from the data

        # draw the tree
        """
            Parse the data with respect to the form and to
            
            create a dictionary such that each entry has the pid and the entries are a list of transactions. 
                this list will define the nodes of the process.
            
            when collecting the data for the dictionary,
                - use <from> as the key
                - all items with values of <to> corresponding to <form>
                    ** create a tree with dict, such that: {key:TreeProcessModel(myPid, parentPid, childrenPids)}
                        - to get the processes, collect all <from>'s and create a set from them
                        - iterate over the json data again and attach to the dict of <from>'s <to>'s that sent to the <from>
                    ** create playback instances. 
                        - a list of classes PlaybackInstance(from, to, action, data) => instances of the class is data from the json file
                        - order the playback instances list by send_time in increasing order.
                        -
                    
                ===== or =====
                - we attach the tree process structure to the tree incoming server data. this way we can just read the 
                    data off and not worry about re constructing the tree based on the data.
                    - if we do it like this. we would then use then
                        - parse the snapshots by timestamps in increasing order
                        - draw arrows at each line showing the states happening.
                        
                ++ thoughts:
                    We can leave each process colorless and use arrows to indicate the flow of data.
                    - we define each QGraphics object to be clickable and should have and id, such that on clicked we 
                        go the list of actions and get the thing that happened at that stage and then render it 
                        in the properties section.
                        - Check if we collect process state data from the source
            
            draw the processes vertically. with each node equidistant from the other.
                - connect the first node of each process to its respectively parent by a line
                    - define each node to have the for attachemnt points NSEW, where the node connections are as follows
                        - parent.SOUTH -> current.NORTH
                        - current.SOUTH -> child. NORTH
                        - current.EAST -> rightChild.NORTH
                    - At the end of the child, attatch a short line that indicates carries the process id at the end.
        """


    def load_json_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.output_text_edit.append("JSON Loaded")
                return data
        except FileNotFoundError:
            self.output_text_edit.append(f"The file '{file_path}' was not found.")
            return None
        except json.JSONDecodeError:
            self.output_text_edit.append(f"The file '{file_path}' does not contain valid JSON.")
            return None


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
