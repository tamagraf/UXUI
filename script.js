
async function getQuestion() {
    const response = await fetch('/get_question');
    const question = await response.json();
    const container = document.getElementById('question-container');
    container.innerHTML = `<p>${question.text}</p>
        <ul>${question.options.map((option, i) => `<li>${option}</li>`).join('')}</ul>`;
}
