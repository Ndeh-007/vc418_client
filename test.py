import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtCore import QProcess, Slot


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

        self.start_process_button = QPushButton("Run Command")
        self.start_process_button.clicked.connect(self.start_process)
        self.layout.addWidget(self.start_process_button)

    @Slot()
    def start_process(self):
        # Set the command to run here

        # Connect process signals
        self.process.readyReadStandardOutput.connect(self.read_output)
        self.process.readyReadStandardError.connect(self.read_error)
        self.process.errorOccurred.connect(self.handle_error)

        # Start the process
        self.process.start('rebar3',['plugins'])

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


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
