'use strict'
import { useState, } from 'react'
import Head from 'next/head'
import Header from './header'
import Footer from './footer'
import QuestionForm from './question-form'
import EightBall from './eight-ball'
import History from './history'

export default function MagicEightBallGame(props) {

    const { answeredQuestions, error, post } = props.useAnsweredQuestions();

    const { replies, repliesError } = props.useReplies();

    const [waiting, setWaiting] = useState(true);

    if (error || repliesError) {
        props.onLogout()
        return null;
    }

    if (!(answeredQuestions && replies)) return <h2>Loading...</h2>

    async function questionAskedHandler(question) {

        post({ question, reply: getRandomReply() });

        setWaiting(false);
    }

    function getRandomReply() {

        const randIndex = Math.floor(Math.random() * replies.length);

        return replies[randIndex];
    }

    function getLatestAnsweredQuestion() {
        return waiting ? null : answeredQuestions[answeredQuestions.length - 1];
    }

    return (
        <div>
            <Head>
                <title>Magic 8 Ball</title>
            </Head>

            <Header answerCount={answeredQuestions.length}
                onLogout={props.onLogout}
                username={props.username} />

            <QuestionForm onQuestionAsked={questionAskedHandler} />
            <EightBall answeredQuestion={getLatestAnsweredQuestion()} />
            <History answeredQuestions={answeredQuestions} />
            <Footer />
        </div>
    );
}
