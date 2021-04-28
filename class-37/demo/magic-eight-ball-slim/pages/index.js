import Head from 'next/head'
import { useState } from 'react'

export default function Home() {

    const [reply, setReply] = useState("Ask me anything");
    const [question, setQuestion] = useState('thinking...')

    function questionAskedHandler(event) {

        event.preventDefault();

        const randomReply = Math.random() > .5 ? "Yes" : "No";

        setReply(randomReply);

        setQuestion(event.target.question.value);
    }

    return (
        <div className="">
            <Head>
                <title>Magic Eight Ball</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <Header title="Magic Eight Ball" />

            <main className="">

                <QuestionForm onSubmit={questionAskedHandler} />

                <EightBall reply={reply} question={question} />

            </main>

            <Footer author="Code Fellows" />
        </div>
    )
}

function Header(props) {
    return (
        <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
            <h1 className="text-4xl">{props.title}</h1>
        </header>
    );
}

function Footer(props) {
    return (
        <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
            <p>{props.author}</p>
        </footer>
    );
}

function EightBall(props) {
    return (
        <div>
            <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
                <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                    <p className="text-xl text-center">{props.reply}</p>
                </div>
            </div>
            <h3 className="text-2xl text-center">{props.question}</h3>
        </div>
    );
}

function QuestionForm(props) {
    return (
        <form onSubmit={props.onSubmit} className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
            <input className="flex-auto pl-1" name="question" />
            <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
        </form>
    );
}
