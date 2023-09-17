import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate

def on_month_changed():
    selected_date = calendar.selectedDate()
    label.setText(f"Selected Date: {selected_date.toString('MMMM yyyy')}")

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PyQt5 Calendar Example")
window.setGeometry(100, 100, 400, 400)

calendar = QCalendarWidget(window)
calendar.setGeometry(50, 50, 300, 200)

# Set the calendar to the current month
current_date = QDate.currentDate()
calendar.setSelectedDate(current_date)

# Create a label to display selected date
label = QLabel(window)
label.setGeometry(50, 260, 300, 30)

# Connect the signal for month change
calendar.currentPageChanged.connect(on_month_changed)

window.show()
sys.exit(app.exec_())
