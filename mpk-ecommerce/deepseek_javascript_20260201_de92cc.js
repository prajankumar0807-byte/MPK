function initiateUPIPayment(amount, buyerUPI) {
    // In real scenario, integrate with payment gateway like Razorpay
    // This is a simulation
    const upiLink = `upi://pay?pa=${buyerUPI}&pn=MPK_Store&am=${amount}&tn=Payment for order`;
    
    // Open UPI app or show QR code
    window.location.href = upiLink;
    
    // After payment success
    fetch('/confirm-payment', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            order_id: getOrderId(),
            upi_id: buyerUPI,
            amount: amount
        })
    });
}