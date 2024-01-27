
// Function to calculate Loan Payment on the website 
function calculateLoanPayment() {
  const loanAmount = document.getElementById("loan-amount").value;
  const interestRate = document.getElementById("interest-rate").value / 100 / 12;
  const loanTerm = document.getElementById("loan-term").value;
  const monthlyPayment = (loanAmount * interestRate * Math.pow(1 + interestRate, loanTerm)) / (Math.pow(1 + interestRate, loanTerm) - 1);
  document.getElementById("monthly-payment").innerHTML = "Monthly Payment: $" + monthlyPayment.toFixed(2);
}