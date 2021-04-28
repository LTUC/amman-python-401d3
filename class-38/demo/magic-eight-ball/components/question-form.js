export default function QuestionForm({ onAnswer }) {

    const registerUser = event => {
        event.preventDefault() // don't redirect the page
        // where we'll add our form logic
        onAnswer(event.target.question.value);
    }

    return (
        <form onSubmit={registerUser} className="flex w-1/2 p-4 mx-auto my-8 bg-gray-200 rounded-sm">
            <input className="w-full px-2 py-2 text-2xl" id="question" type="text" placeholder="Ask anything" required />
            <button type="submit" className="px-4 py-2 bg-gray-500 text-gray-50">Ask</button>
        </form>
    );

}
