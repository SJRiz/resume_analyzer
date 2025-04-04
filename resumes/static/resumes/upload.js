function disableSubmitButton() {
    document.getElementById("submit-button").disabled = true; // Can only submit once
    document.getElementById("spinner").style.display = "inline-block"; // Show spinner
}