// Get references to HTML elements
// Initialize the speech synthesis object

// Function to read the text
function speakText() {
    const text = "This is about fidelity investment
    Accessibility is a major key to the success of Fidelity Investments, as it reflects the company's commitment to inclusivity, legal compliance, and customer satisfaction. By ensuring that their financial services and technology are accessible to individuals with disabilities, Fidelity not only expands its customer base but also upholds ethical business practices and builds a reputation as a socially responsible and customer-centric financial services provider. Additionally, accessibility promotes financial inclusion, helping individuals with disabilities achieve their financial goals and contributes to a diverse and inclusive workforce.
    Some of the tips to invest wisely are:
    
    The first tip is Diversify your portfolio
    Diversification involves spreading your investments across a variety of asset classes, such as stocks, bonds, real estate, and commodities. By doing so, you can reduce the risk associated with individual investments and improve your overall portfolio stability.
    
    The second tip is Invest for the Long Term
    Investing with a long-term perspective allows you to ride out market fluctuations and benefit from the power of compounding. Historically, the stock market has shown a tendency to rise over the long run, despite short-term volatility.
    
    The third tip is Do Your Research
    Before making any investment, conduct thorough research on the asset or investment vehicle you're considering. Understand the company's fundamentals, the market conditions, and any potential risks associated with the investment.
    
    The fourth tip is Clear Investment Goals
    Determine your financial objectives and time horizon for each investment. Whether you're saving for retirement, a major purchase, or a child's education, having specific goals in mind will help you make appropriate investment choices and track your progress.
    
    The fifth tip is Manage Risk Appropriately
    Understand your risk tolerance and invest accordingly. Conservative investors may prefer safer assets like bonds, while those with a higher risk tolerance may allocate more to stocks. Your asset allocation should align with your comfort level and long-term financial objectives.
    "
    ;
    const speech = new SpeechSynthesisUtterance();

    // Set the text to be spoken
    speech.text = text;

    // Use the browser's built-in speech synthesis to speak the text
    window.speechSynthesis.speak(speech);
}

// Add click event listener to the "Speak" button
const button = document.getElementById("textToSpeechButton");
button.addEventListener("click", speakText);
