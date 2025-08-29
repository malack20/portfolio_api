// A simple script to add a dynamic effect to the content on page load

document.addEventListener('DOMContentLoaded', () => {
    // Select the main content container
    const contentContainer = document.querySelector('.content-container');

    // Add a class to the container to trigger a CSS animation
    // This example uses a class that might be added to trigger a specific effect
    if (contentContainer) {
        // You could add a simple class to signify the content has loaded
        // For our purpose, the CSS already handles this with the keyframe animation
        console.log("Page loaded. Content container found.");
    }

    // Example of a simple interactive feature: a message box
    // This is a safer alternative to alert()
    const message = "Welcome to the backend! This is a dynamic message from your script.js file.";
    console.log(message);

    // You could also have code here to handle form submissions,
    // API calls, or other dynamic behaviors.
});