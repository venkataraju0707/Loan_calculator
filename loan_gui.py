import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LoanCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Loan Calculator')
        self.setGeometry(100, 100, 300, 200)

        self.amount_label = QLabel('Loan Amount:')
        self.amount_input = QLineEdit()
        
        self.rate_label = QLabel('Interest Rate (%):')
        self.rate_input = QLineEdit()
        
        self.term_label = QLabel('Loan Term (years):')
        self.term_input = QLineEdit()

        self.result_label = QLabel('')
        
        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_loan)

        layout = QVBoxLayout()
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.rate_label)
        layout.addWidget(self.rate_input)
        layout.addWidget(self.term_label)
        layout.addWidget(self.term_input)
        layout.addWidget(self.result_label)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate_loan(self):
        amount = float(self.amount_input.text())
        rate = float(self.rate_input.text()) / 100
        term = int(self.term_input.text())
        
        monthly_payment = (amount * rate / 12) / (1 - (1 + rate / 12) ** (-term * 12))
        total_payment = monthly_payment * term * 12
        total_interest = total_payment - amount

        result_text = f'Monthly Payment: ${monthly_payment:.2f}\n'
        result_text += f'Total Payment: ${total_payment:.2f}\n'
        result_text += f'Total Interest: ${total_interest:.2f}'
        self.result_label.setText(result_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = LoanCalculator()
    calculator.show()
    sys.exit(app.exec_())
