from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Python Calculator")
main_window.resize(250, 300)

# Main text box styling
text_box = QLineEdit()
text_box.setAlignment(Qt.AlignRight)
text_box.setFont(QFont("Arial", 20))
text_box.setStyleSheet("""
    QLineEdit {
        background-color: #1e1e1e;   /* Python blue */
        color: #FFD43B;              /* Python yellow */
        border: 2px solid #4B8BBE;
        border-radius: 8px;
        padding: 10px;
    }
""")

# Create grid layout for the buttons
grid = QGridLayout()

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", ">", "+"
]

# Clear and equals buttons
clear = QPushButton("Clear")
equals = QPushButton("=")

# Function for handling button clicks
def button_click():
    button = app.sender()
    text = button.text()
    
    if text == "=":
        expression = text_box.text()
        try:
            result = eval(expression)
            text_box.setText(str(result))
        except Exception as e:
            text_box.setText("Error")
    
    elif text == "Clear":
        text_box.clear()
    
    elif text == ">":
       current_text = text_box.text()
       text_box.setText(current_text[:-1])
    else:
        current_text = text_box.text()
        text_box.setText(current_text + text)

# Set up grid layout for buttons
col = 0
row = 0
for text in buttons:
    button = QPushButton(text)
    button.setFont(QFont("Arial", 15))
    button.clicked.connect(button_click)
    button.setStyleSheet("""
        QPushButton {
            background-color: #1e1e1e;
            color: white;
            border-radius: 8px;
            border: 2px solid #306998;
            padding: 12px;
        }
        QPushButton:hover {
            background-color: #FFD43B;
            color: black;
        }
        QPushButton:pressed {
            background-color: #FFE873;
        }
    """)
    grid.addWidget(button, row, col)
    col += 1 
    if col > 3:
        col = 0
        row += 1

# Style for Clear and Equals buttons
clear.setFont(QFont("Arial", 15))
clear.setStyleSheet("""
    QPushButton {
        background-color: #ffffff;   /* Distinct red for clear */
        color: black;
        border-radius: 8px;
        padding: 12px;
    }
    QPushButton:hover {
        background-color: #FF7F71;
    }
    QPushButton:pressed {
        background-color: #FF5F51;
    }
""")
equals.setFont(QFont("Arial", 15))
equals.setStyleSheet("""
    QPushButton {
        background-color: #ffffff;   /* Same color as clear */
        color: black;
        border-radius: 8px;
        padding: 12px;
    }
    QPushButton:hover {
        background-color: #FF7F71;
    }
    QPushButton:pressed {
        background-color: #FF5F51;
    }
""")

# Master layout
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

# Row for Clear and Equals buttons
button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(equals)
master_layout.addLayout(button_row)

# Apply layout to main window
main_window.setLayout(master_layout)

# Connect Clear and Equals buttons to click handler
clear.clicked.connect(button_click)
equals.clicked.connect(button_click)

# Main window styling
main_window.setStyleSheet("""
    QWidget {
        background-color: #2B2B2B;   /* Dark background */
    }
""")

# Show the main window
main_window.show()
app.exec()
