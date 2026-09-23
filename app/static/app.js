const button = document.getElementById("next-button");
const problemInput = document.getElementById("problem");

const result = document.getElementById("result");
const action = document.getElementById("action");
const reason = document.getElementById("reason");
const errorMessage = document.getElementById("error-message");

button.addEventListener("click", getNextAction);

problemInput.addEventListener("keydown", (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
        getNextAction();
    }
});

async function getNextAction() {
    const problem = problemInput.value.trim();

    if (!problem) {
        problemInput.focus();
        return;
    }

    button.disabled = true;
    button.querySelector("span:first-child").textContent = "Thinking...";
    errorMessage.hidden = true;

    try {
        const response = await fetch("/api/next", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                problem: problem
            })
        });

        if (!response.ok) {
            throw new Error("Request failed");
        }

        const data = await response.json();

        action.textContent = data.action;
        reason.textContent = data.reason;

        result.hidden = false;
        result.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    } catch (error) {
        errorMessage.textContent =
            "We couldn't get your next action. Please try again.";
        errorMessage.hidden = false;
    } finally {
        button.disabled = false;
        button.querySelector("span:first-child").textContent = "NEXT";
    }
}